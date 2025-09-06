from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        model_config = ConfigDict(from_attributes=True)

# Client schemas
class ClientBase(BaseModel):
    name: str
    email: str
    phone: str

class ClientCreate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id: int
    created_at: datetime

    class Config:
        model_config = ConfigDict(from_attributes=True) 