from __future__ import annotations

from pydantic import BaseModel, Field


class Customcharacterdata(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    customcharacterdataid: int = Field(None, title='Customcharacterdataid')
    characterid: int = Field(None, title='Characterid')
    customfieldname: str = Field(None, title='Customfieldname')
    fieldvalue: str = Field(None, title='Fieldvalue')
