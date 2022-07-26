from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Worldservers(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    worldserverid: int = Field(None, title='Worldserverid')
    serverip: str = Field(None, title='Serverip')
    maxnumberofinstances: int = Field(None, title='Maxnumberofinstances')
    port: int = Field(None, title='Port')
    serverstatus: int = Field(None, title='Serverstatus')
    internalserverip: str = Field(None, title='Internalserverip')
    startingmapinstanceport: int = Field(None, title='Startingmapinstanceport')
    activestarttime: Optional[datetime] = Field(None, title='Activestarttime')
