from typing import List

from pydantic import BaseModel


class TopicData(BaseModel):
    topicId: str = None
    topic: str = None
    data: List = []


class CaseModel(BaseModel):
    caseName: str = None
    triggerData: TopicData = None
    dataBeforeRun: List[TopicData] = []
    dataAfterRun: List[TopicData] = []
