from app.models.models import item
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.schemas.item import Item_create

router = APIRouter(
    prefix='/payment',
    tags=['payment'],
)

@router.get("/payment/{item_id}")
async def get_specific_payments(item_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(item).where(item.c.id == item_id)
    result = await session.execute(query)
    return result.all()

@router.post("/payment")
async def add_specific_payments(new_payment: Item_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(item).values(**new_payment.dict())
    await session.execute(stmt)
    await  session.commit()
    return {"status": "payment added"}
