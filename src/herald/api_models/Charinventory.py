from __future__ import annotations

from pydantic import BaseModel, Field


class Charinventory(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    characterid: int = Field(None, title='Characterid')
    charinventoryid: int = Field(None, title='Charinventoryid')
    inventoryname: str = Field(None, title='Inventoryname')
    inventorysize: int = Field(None, title='Inventorysize')
    inventorywidth: int = Field(None, title='Inventorywidth')
    inventoryheight: int = Field(None, title='Inventoryheight')
