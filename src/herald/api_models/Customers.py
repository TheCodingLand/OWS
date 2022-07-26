from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Customers(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    customername: str = Field(None, title='Customername')
    customeremail: str = Field(None, title='Customeremail')
    enabledebuglogging: bool = Field(None, title='Enabledebuglogging')
    enableautoloopback: bool = Field(None, title='Enableautoloopback')
    developerpaid: bool = Field(None, title='Developerpaid')
    stripecustomerid: str = Field(None, title='Stripecustomerid')
    supportunicode: bool = Field(None, title='Supportunicode')
    createdate: datetime = Field(None, title='Createdate')
    noportforwarding: bool = Field(None, title='Noportforwarding')
    customerphone: Optional[str] = Field(None, title='Customerphone')
    customernotes: Optional[str] = Field(None, title='Customernotes')
    publisherpaiddate: Optional[datetime] = Field(None, title='Publisherpaiddate')
    freetrialstarted: Optional[datetime] = Field(None, title='Freetrialstarted')
