from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Areasofinterest(BaseModel):
    customerguid: str = Field(None, title='Customerguid')
    areasofinterestguid: str = Field(None, title='Areasofinterestguid')
    mapzoneid: int = Field(None, title='Mapzoneid')
    areaofinterestname: str = Field(None, title='Areaofinterestname')
    radius: float = Field(None, title='Radius')
    areaofinteresttype: int = Field(None, title='Areaofinteresttype')
    x: Optional[float] = Field(None, title='X')
    y: Optional[float] = Field(None, title='Y')
    z: Optional[float] = Field(None, title='Z')
    rx: Optional[float] = Field(None, title='Rx')
    ry: Optional[float] = Field(None, title='Ry')
    rz: Optional[float] = Field(None, title='Rz')
    customdata: Optional[str] = Field(None, title='Customdata')
