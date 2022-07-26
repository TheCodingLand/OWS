from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Abilities(BaseModel):
    class_: Optional[int] = Field(None, title='Class ')
    customerguid: str = Field(None, title='Customerguid')
    abilityid: int = Field(None, title='Abilityid')
    abilityname: str = Field(None, title='Abilityname')
    abilitytypeid: int = Field(None, title='Abilitytypeid')
    texturetouseforicon: str = Field(None, title='Texturetouseforicon')
    gameplayabilityclassname: str = Field(None, title='Gameplayabilityclassname')
    race: Optional[int] = Field(None, title='Race')
    abilitycustomjson: Optional[str] = Field(None, title='Abilitycustomjson')
