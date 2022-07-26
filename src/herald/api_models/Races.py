from __future__ import annotations

from pydantic import BaseModel, Field


class Races(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    raceid: int = Field(None, title='Raceid')
    racename: str = Field(None, title='Racename')
