from sqlalchemy import Table, Column, String, Integer, String, MetaData, ForeignKey, TIMESTAMP, Boolean
from datetime import datetime

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=True),
    Column("username", String, nullable=False, unique=True),
    Column("email", String, nullable=False, unique=True),
    Column("password", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow)
)

item = Table(
    "item",
    metadata,
    Column("product_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("price", Integer, nullable=False, unique=True),
    Column("description", String, nullable=False, unique=True),
    Column("created_at", TIMESTAMP, default=datetime.utcnow)
)

order = Table(
    "order",
    metadata,
    Column("order_id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("user.user_id")),
    Column("status", String, nullable=False),
    Column("price", Integer, ForeignKey("item.item_id")),
    Column("created_at", TIMESTAMP, default=datetime.utcnow)
)
