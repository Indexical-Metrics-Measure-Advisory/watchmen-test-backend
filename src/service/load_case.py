import json
from os import walk

from src.model.case import CaseModel


def load_cases_in_folder(folder):
    _, _, filenames = next(walk(folder))
    cases = []
    for file_name in filenames:
        with open(folder + "/" + file_name) as f:
            case: CaseModel = CaseModel.parse_obj(json.load(f))
            case.caseName = file_name
            cases.append(case)
    return cases


def load_case(file_path):
    with open(file_path) as f:
        case: CaseModel = CaseModel.parse_obj(json.load(f))
        case.caseName = file_path
        return case
