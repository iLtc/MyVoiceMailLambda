from twilio.twiml.voice_response import VoiceResponse
import google


def main(event, context):
    resp = VoiceResponse()

    resp.say("Thank you for calling! Have a great day.", voice='alice')

    return {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'text/xml',
        },
        "body": str(resp)
    }


if __name__ == '__main__':
    print(main(None, None))
