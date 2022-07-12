from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class CorrectCompany(BaseModel):

    uid: int
    name: str = Field(min_length=2)
    region: str = Field(min_length=2)
    category: str = Field(min_length=2)
    description: str


MAX_JOB_DESCRIPTION = 4000


class CorrectJob(BaseModel):

    uid: int
    name: str = Field(min_length=2)
    company_uid: int = Field(ge=1)
    salary: Optional[int]
    description: Optional[str] = Field(max_length=MAX_JOB_DESCRIPTION)
    date_published: Optional[date]
    date_expiring: Optional[date]
    url: str
