import json
from pprint import pprint


def config():
    json_data = open('config.json').read()

    data = json.loads(json_data)

    return data


if __name__ == '__main__':
    pprint(config())
