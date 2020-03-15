import json


def extract_data():
    data = {}
    data['timeline'] = []
    with open('data/timeline.txt') as json_file:
        data['timeline'] = json.load(json_file)
        json_file.close()
        return data['timeline']
