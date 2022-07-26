from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Charinventoryitems(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    charinventoryid: int = Field(None, title='Charinventoryid')
    charinventoryitemid: int = Field(None, title='Charinventoryitemid')
    itemid: int = Field(None, title='Itemid')
    inslotnumber: int = Field(None, title='Inslotnumber')
    quantity: int = Field(None, title='Quantity')
    numberofusesleft: int = Field(None, title='Numberofusesleft')
    condition: int = Field(None, title='Condition')
    charinventoryitemguid: str = Field(None, title='Charinventoryitemguid')
    customdata: Optional[str] = Field(None, title='Customdata')
