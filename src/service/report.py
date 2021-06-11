from typing import List

import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from src.model.test_result import TestResult


def __build_table_list(results: List[TestResult]):
    result_list = []
    for result in results:
        for topic_result in result.topicResults:
            result_list.append(
                [result.caseName, result.rawTopicName, topic_result.topicName, topic_result.instanceCount,
                 topic_result.expectedCount,
                 topic_result.countMatch])

    return result_list


def generate_pdf_report(results, site, pdf=None):
    env = Environment(loader=FileSystemLoader('src'))
    template = env.get_template("report-template.html")
    records = __build_table_list(results)
    table = pd.DataFrame.from_records(records, columns=["caseName", "rawTopicName", "topicName", "instanceCount",
                                                        "expectedCount",
                                                        "countMatch"])
    #
    template_vars = {"title": site, "records": table.to_html()}
    html_out = template.render(template_vars)
    if pdf:
        HTML(string=html_out).write_pdf("pdf/" + pdf + ".pdf", stylesheets=["./src/style.css"])
    else:
        HTML(string=html_out).write_pdf("pdf/report.pdf", stylesheets=["./src/style.css"])
    print("generate_pdf_report")
