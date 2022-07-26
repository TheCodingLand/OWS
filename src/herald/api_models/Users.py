from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Users(BaseModel):
    userguid: str = Field(None, title='Userguid')
    customerguid: str = Field(None, title='Customerguid')
    firstname: str = Field(None, title='Firstname')
    lastname: str = Field(None, title='Lastname')
    email: str = Field(None, title='Email')
    passwordhash: str = Field(None, title='Passwordhash')
    createdate: datetime = Field(None, title='Createdate')
    lastaccess: datetime = Field(None, title='Lastaccess')
    role: str = Field(None, title='Role')
