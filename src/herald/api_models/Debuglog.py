from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Debuglog(BaseModel):
    debuglogid: int = Field(None, title='Debuglogid')
    debugdate: Optional[datetime] = Field(None, title='Debugdate')
    debugdesc: Optional[str] = Field(None, title='Debugdesc')
    customerguid: Optional[str] = Field(None, title='Customerguid')
