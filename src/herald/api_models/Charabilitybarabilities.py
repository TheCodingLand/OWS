from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Charabilitybarabilities(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    charabilitybarabilityid: int = Field(None, title='Charabilitybarabilityid')
    charabilitybarid: int = Field(None, title='Charabilitybarid')
    charhasabilitiesid: int = Field(None, title='Charhasabilitiesid')
    inslotnumber: int = Field(None, title='Inslotnumber')
    charabilitybarabilitiescustomjson: Optional[str] = Field(
        None, title='Charabilitybarabilitiescustomjson'
    )
