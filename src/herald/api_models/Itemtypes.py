from __future__ import annotations

from pydantic import BaseModel, Field


class Itemtypes(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    itemtypeid: int = Field(None, title='Itemtypeid')
    itemtypedesc: str = Field(None, title='Itemtypedesc')
    useritemtype: int = Field(None, title='Useritemtype')
    equipmenttype: int = Field(None, title='Equipmenttype')
    itemquality: int = Field(None, title='Itemquality')
    equipmentslottype: int = Field(None, title='Equipmentslottype')
