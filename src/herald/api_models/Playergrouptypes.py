from __future__ import annotations

from pydantic import BaseModel, Field


class Playergrouptypes(BaseModel):
    playergrouptypeid: int = Field(None, title='Playergrouptypeid')
    playergrouptypedesc: str = Field(None, title='Playergrouptypedesc')
