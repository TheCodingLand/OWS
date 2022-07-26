from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Charabilitybars(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    charabilitybarid: int = Field(None, title='Charabilitybarid')
    characterid: int = Field(None, title='Characterid')
    abilitybarname: str = Field(None, title='Abilitybarname')
    maxnumberofslots: int = Field(None, title='Maxnumberofslots')
    numberofunlockedslots: int = Field(None, title='Numberofunlockedslots')
    charabilitybarscustomjson: Optional[str] = Field(
        None, title='Charabilitybarscustomjson'
    )
