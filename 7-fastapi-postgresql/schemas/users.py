
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: str #EmailStr
    fullname: str
    is_superuser: bool
    
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    fullname: str
    is_superuser: Optional[bool] = None
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Optional[str] = None
    id: Optional[int] = None