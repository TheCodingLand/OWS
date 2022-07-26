from __future__ import annotations

from pydantic import BaseModel, Field


class Chatgroupusers(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    chatgroupid: int = Field(None, title='Chatgroupid')
    characterid: int = Field(None, title='Characterid')
