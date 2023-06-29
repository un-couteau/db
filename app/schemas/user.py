from pydantic import BaseModel
from datetime import datetime
class User_create(BaseModel):
    user_id: int
    username: str
    email: str
    created_at: datetime
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool