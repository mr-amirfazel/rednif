import json


def json_reader(path):
    f = open(path)
    data = json.load(f)
    return data
