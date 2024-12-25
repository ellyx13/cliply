from datetime import datetime
from typing import List

from core.data_type import UrlStr
from pydantic import BaseModel


class Articles(BaseModel):
    title: str
    url: UrlStr
    domain: str
    summary: str
    keywords: List[str]
    category: str
    created_at: datetime
