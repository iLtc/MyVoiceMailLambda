from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account
from config import config

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

SERVICE_ACCOUNT_FILE = 'account.json'

calendarIds = config()['calendarIds']


def next_event_time():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=credentials)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    all_events = []

    for cid in calendarIds:
        events_result = service.events().list(calendarId=cid, timeMin=now,
                                              maxResults=3, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if len(events) > 0:
            for event in events:
                if 'dateTime' in event['start']:
                    all_events.append(event)

    all_events.sort(key=lambda x: x['start']['dateTime'])

    if not all_events:
        return False

    return all_events[0]['start']['dateTime']


if __name__ == '__main__':
    print(next_event_time())
