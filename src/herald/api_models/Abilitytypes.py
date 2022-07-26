from __future__ import annotations

from pydantic import BaseModel, Field


class Abilitytypes(BaseModel):
    abilitytypeid: int = Field(None, title='Abilitytypeid')
    abilitytypename: str = Field(None, title='Abilitytypename')
    customerguid: str = Field(None, title='Customerguid')
