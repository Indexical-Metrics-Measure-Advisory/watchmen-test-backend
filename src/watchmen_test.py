# import json
# from enum import Enum
# from os import path

import os

from src.service.import_init_data import init_master_data
from src.service.load_case import load_cases_in_folder, load_case
from src.service.report import generate_pdf_report
from src.service.site_service import load_site_json, save_to_json
from src.service.test_case_execute import execute_cases, execute


class WatchmenTest(object):
    """
    :authors: imma-team
    :version: 1.0
    """

    def add_site(self, name, host, username=None, password=None):
        """ add_site {site_name} {host_url} {username} {password}
        """
        sites = load_site_json()
        sites[name] = {"host": host, "username": username, "password": password}
        save_to_json(sites)

    def test(self, path, site,init=False,clean=True,pdf=None):
        print("test in ",path)
        sites = load_site_json()
        if os.path.isdir(path):
            print(path)
            if init:
                init_master_data(sites[site],path)
            cases = load_cases_in_folder(path)
            results = execute_cases(cases, sites[site],clean)
            print(results)
            generate_pdf_report(results,site,pdf)
        elif os.path.isfile(path):
            case = load_case(path)
            result = execute(case,sites[site])
            generate_pdf_report([result], site, pdf)
