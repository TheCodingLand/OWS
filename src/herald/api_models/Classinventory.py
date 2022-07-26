from __future__ import annotations

from pydantic import BaseModel, Field


class Classinventory(BaseModel):
    classinventoryid: int = Field(None, title='Classinventoryid')
    customerguid: str = Field(None, title='Customerguid')
    classid: int = Field(None, title='Classid')
    inventoryname: str = Field(None, title='Inventoryname')
    inventorysize: int = Field(None, title='Inventorysize')
    inventorywidth: int = Field(None, title='Inventorywidth')
    inventoryheight: int = Field(None, title='Inventoryheight')
