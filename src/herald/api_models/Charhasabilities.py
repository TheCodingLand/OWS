from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Charhasabilities(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    charhasabilitiesid: int = Field(None, title='Charhasabilitiesid')
    characterid: int = Field(None, title='Characterid')
    abilityid: int = Field(None, title='Abilityid')
    abilitylevel: int = Field(None, title='Abilitylevel')
    charhasabilitiescustomjson: Optional[str] = Field(
        None, title='Charhasabilitiescustomjson'
    )
