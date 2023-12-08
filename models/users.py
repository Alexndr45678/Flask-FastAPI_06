from pydantic import BaseModel, Field

class UserIn(BaseModel):
    first_name: str = Field(..., max_length=32)
    last_name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)
    password: str = Field(..., min_length=8)

class User(BaseModel):
    id: int
    first_name: str = Field(..., max_length=32)
    last_name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)
    