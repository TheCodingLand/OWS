from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Mapinstances(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    mapinstanceid: int = Field(None, title='Mapinstanceid')
    worldserverid: int = Field(None, title='Worldserverid')
    mapid: int = Field(None, title='Mapid')
    port: int = Field(None, title='Port')
    status: int = Field(None, title='Status')
    numberofreportedplayers: int = Field(None, title='Numberofreportedplayers')
    createdate: datetime = Field(None, title='Createdate')
    playergroupid: Optional[int] = Field(None, title='Playergroupid')
    lastupdatefromserver: Optional[datetime] = Field(None, title='Lastupdatefromserver')
    lastserveremptydate: Optional[datetime] = Field(None, title='Lastserveremptydate')
