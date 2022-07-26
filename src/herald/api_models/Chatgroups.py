from __future__ import annotations

from pydantic import BaseModel, Field


class Chatgroups(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    chatgroupid: int = Field(None, title='Chatgroupid')
    chatgroupname: str = Field(None, title='Chatgroupname')
