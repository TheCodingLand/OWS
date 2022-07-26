from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Playergroup(BaseModel):
    playergroupid: int = Field(None, title='Playergroupid')
    customerguid: str = Field(None, title='Customerguid')
    playergroupname: str = Field(None, title='Playergroupname')
    playergrouptypeid: int = Field(None, title='Playergrouptypeid')
    readystate: int = Field(None, title='Readystate')
    createdate: Optional[datetime] = Field(None, title='Createdate')
