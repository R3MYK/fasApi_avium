from pydantic import BaseModel #Libreria para modelo de datos

from typing import Optional #libreria para definir tipo de datos

#Schema de la tabla User
class UserSchema(BaseModel):
    user_cod: Optional[int] = None
    user_pass: str
    user_rut: int
    user_name: str
    user_last_name: str
    profile_cod: int
