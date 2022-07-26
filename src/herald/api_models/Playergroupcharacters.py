from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Playergroupcharacters(BaseModel):
    playergroupid: int = Field(None, title='Playergroupid')
    customerguid: str = Field(None, title='Customerguid')
    characterid: int = Field(None, title='Characterid')
    dateadded: datetime = Field(None, title='Dateadded')
    teamnumber: int = Field(None, title='Teamnumber')
