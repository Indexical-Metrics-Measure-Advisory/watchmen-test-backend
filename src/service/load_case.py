import json
from os import walk

from src.model.case import CaseModel


def load_cases_in_folder(folder):
    _, _, filenames = next(walk(folder))
    cases = []

    for file_name in filenames:
        if file_name != "topic.json" and file_name != "pipeline.json":
            with open(folder + "/" + file_name,encoding="utf-8") as f:
                case: CaseModel = CaseModel.parse_obj(json.load(f))
                case.caseName = file_name
                cases.append(case)
    return cases


def load_topic_list_in_folder(folder):
    _, _, filenames = next(walk(folder))
    # print("filenames",filenames)
    for file_name in filenames:
        if file_name == "topic.json":
            with open(folder + "/" + file_name,encoding="utf-8") as f:
                return json.load(f)


def load_pipeline_list_in_folder(folder):
    _, _, filenames = next(walk(folder))

    for file_name in filenames:
        print(file_name)
        if file_name == "pipeline.json":
            with open(folder + "/" + file_name,encoding="utf-8") as f:
                return json.load(f)


def load_case(file_path):
    with open(file_path) as f:
        case: CaseModel = CaseModel.parse_obj(json.load(f))
        case.caseName = file_path
        return case
