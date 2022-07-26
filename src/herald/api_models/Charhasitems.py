from __future__ import annotations

from pydantic import BaseModel, Field


class Charhasitems(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    characterid: int = Field(None, title='Characterid')
    charhasitemid: int = Field(None, title='Charhasitemid')
    itemid: int = Field(None, title='Itemid')
    quantity: int = Field(None, title='Quantity')
    equipped: bool = Field(None, title='Equipped')
