from __future__ import annotations

from pydantic import BaseModel, Field


class Globaldata(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    globaldatakey: str = Field(None, title='Globaldatakey')
    globaldatavalue: str = Field(None, title='Globaldatavalue')
