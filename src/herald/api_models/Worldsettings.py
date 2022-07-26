from __future__ import annotations

from pydantic import BaseModel, Field


class Worldsettings(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    worldsettingsid: int = Field(None, title='Worldsettingsid')
    starttime: int = Field(None, title='Starttime')
