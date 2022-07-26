from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Usersessions(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    usersessionguid: str = Field(None, title='Usersessionguid')
    userguid: str = Field(None, title='Userguid')
    logindate: datetime = Field(None, title='Logindate')
    selectedcharactername: Optional[str] = Field(None, title='Selectedcharactername')
