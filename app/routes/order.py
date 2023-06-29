from app.models.models import order
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.schemas.order import Order_create

router = APIRouter(
    prefix='/tariff',
    tags=['tariff'],
)

@router.get("/order/{order_id}")
async def get_specific_tariffs(order_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(order).where(order.c.id == order_id)
    result = await session.execute(query)
    return result.all()

@router.post("/order")
async def add_specific_tariffs(new_order: Order_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(order).values(**new_order.dict())
    await session.execute(stmt)
    await  session.commit()
    return {"status": "tariff added"}
