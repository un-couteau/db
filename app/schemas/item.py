from pydantic import BaseModel
from datetime import datetime


class Item_create(BaseModel):
    product_id: int
    name: str
    price: str
    description: str
    created_at: datetime
