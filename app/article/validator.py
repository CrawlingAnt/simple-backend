from pydantic import BaseModel
from typing import Optional, List


class AddArticle(BaseModel):
    title: str
    content_json: str
    content_html: str
    author_id: int

