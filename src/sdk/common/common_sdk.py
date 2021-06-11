import json

import requests

from src.sdk.auth.auth_sdk import login
from src.utils.header_utils import build_headers


def import_instances(instances, site=None):
    headers = build_headers(login(site))
    results = []
    for instance in instances:
        response = requests.post(site["host"] + "topic/data", data=json.dumps(instance),
                                 headers=headers)
        results.append(response.json())
    return results


def remove_topic_collection(collections, site):
    headers = build_headers(login(site))
    response = requests.post(site["host"] + "topic/data/remove", data=json.dumps(collections),
                             headers=headers)
    # print(response.status_code)


def get_value_from_subject(query, site):
    headers = build_headers(login(site))
    response = requests.post(site["host"] + "subject/query", data=json.dumps(query), headers=headers)
    return response.json()


def load_topic_data_all(topic_name, site):
    headers = build_headers(login(site))
    response = requests.get(site["host"] + "topic/data/all?topic_name=" + topic_name, headers=headers)
    return response.json()
