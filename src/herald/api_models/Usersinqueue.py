from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Usersinqueue(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    userguid: str = Field(None, title='Userguid')
    queuename: str = Field(None, title='Queuename')
    joindt: datetime = Field(None, title='Joindt')
    matchmakingscore: int = Field(None, title='Matchmakingscore')
