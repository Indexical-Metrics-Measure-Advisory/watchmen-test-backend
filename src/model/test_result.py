from typing import List, Any

from pydantic import BaseModel


class FactorNotMatch(BaseModel):
    factorName: str = None
    value: Any = None
    expectedValue: Any = None


class TopicTestResult(BaseModel):
    topicName: str = None
    countMatch: bool = False
    expectedCount: int = None
    instanceCount: int = None
    factorNotMatchList: List[FactorNotMatch] = []


class TestResult(BaseModel):
    caseName: str = None
    rawTopicName: str = None
    prepareTopicName: List[str] = []
    topicResults: List[TopicTestResult] = []
