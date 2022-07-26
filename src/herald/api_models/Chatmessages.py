from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Chatmessages(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    chatmessageid: int = Field(None, title='Chatmessageid')
    sentbycharid: int = Field(None, title='Sentbycharid')
    chatmessage: str = Field(None, title='Chatmessage')
    messagedate: datetime = Field(None, title='Messagedate')
    senttocharid: Optional[int] = Field(None, title='Senttocharid')
    chatgroupid: Optional[int] = Field(None, title='Chatgroupid')
