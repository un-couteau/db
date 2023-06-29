from pydantic import BaseModel


class Order_create(BaseModel):
    item_id: int
    price: str
    description: str
