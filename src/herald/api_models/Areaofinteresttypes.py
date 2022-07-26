from __future__ import annotations

from pydantic import BaseModel, Field


class Areaofinteresttypes(BaseModel):
    areaofinteresttypeid: int = Field(None, title='Areaofinteresttypeid')
    areaofinteresttypedesc: str = Field(None, title='Areaofinteresttypedesc')
