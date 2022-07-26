from __future__ import annotations

from pydantic import BaseModel, Field


class Charonmapinstance(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    characterid: int = Field(None, title='Characterid')
    mapinstanceid: int = Field(None, title='Mapinstanceid')
