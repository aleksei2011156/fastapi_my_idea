from typing import Union, Optional
from pydantic import BaseModel


class Registration(BaseModel):
    login: str
    email: str
    password: str
    