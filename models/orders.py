from pydantic import BaseModel, Field


class OrderIn(BaseModel):
    user_id: int = Field(..., ge=0)
    item_id: int = Field(..., ge=0)
    status: int = Field(..., ge=0, le=4)


class Order(BaseModel):
    id: int
    user_id: int = Field(..., ge=0)
    item_id: int = Field(..., ge=0)
    status: int = Field(..., ge=0, le=4)