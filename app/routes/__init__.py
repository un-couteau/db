from .item import router as item_router
from .order import router as order_router
from .user import router as user_router

routes = (
    item_router,
    order_router,
    user_router
)

__all__ = ['routes']