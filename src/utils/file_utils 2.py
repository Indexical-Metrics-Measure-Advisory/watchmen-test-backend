import json


def load_json(path):
    pass


def load_topics():
    with open('scenario/admin/meta_data/topics.json') as f:
        return json.load(f)


def load_spaces():
    with open('scenario/admin/meta_data/spaces.json') as f:
        return json.load(f)


def load_pipelines():
    with open('scenario/admin/meta_data/pipelines.json') as f:
        return json.load(f)


def load_instances():
    with open('scenario/admin/instance_data/instances.json') as f:
        return json.load(f)