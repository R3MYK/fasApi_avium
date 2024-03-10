from pydantic import BaseModel

from typing import Optional

#Schema de la tabla User
class UserSchema(BaseModel):
    user_cod: Optional[str] = None
    user_rut: int
    user_name: str
    user_last_name: str
    profile_cod: int
