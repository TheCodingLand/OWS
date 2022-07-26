from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Maps(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    mapid: int = Field(None, title='Mapid')
    mapname: str = Field(None, title='Mapname')
    width: int = Field(None, title='Width')
    height: int = Field(None, title='Height')
    zonename: str = Field(None, title='Zonename')
    worldcompcontainsfilter: str = Field(None, title='Worldcompcontainsfilter')
    worldcomplistfilter: str = Field(None, title='Worldcomplistfilter')
    mapmode: int = Field(None, title='Mapmode')
    softplayercap: int = Field(None, title='Softplayercap')
    hardplayercap: int = Field(None, title='Hardplayercap')
    minutestoshutdownafterempty: int = Field(None, title='Minutestoshutdownafterempty')
    mapdata: Optional[bytes] = Field(None, title='Mapdata')
