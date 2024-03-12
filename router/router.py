from fastapi import APIRouter, Response 
from schema.user_schema import UserSchema 
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT  #Status
from config.db import engine
from model.user import users
from werkzeug.security import generate_password_hash, check_password_hash #libreria para encriptar
from typing import List



user = APIRouter()
#GET
@user.get("/")
def root():
    return {"message": "Hi, I am Router from Router"}

@user.get('/api/users', response_model = List[UserSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        return result
    
@user.get('/api/user/{user_cod}', response_model=UserSchema)
def get_user(user_cod: int):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.user_cod == user_cod)).first()
        return result


#POST
@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):

    with engine.connect() as conn:

        new_user = data_user.dict() #Crea Diccionario de datos
        new_user["user_pass"] = generate_password_hash(data_user.user_pass, "pbkdf2:sha256:30", 30)
        conn.execute(users.insert().values(new_user))   #Inserta Datos
        conn.commit()   #Guarda datos en la Tabla
        return Response(status_code=HTTP_201_CREATED)
        #print (data_user)
        #print (new_user)
    
#PUT
@user.put("/api/user/{user_cod}", response_model=UserSchema) #Definir siempre response model

def update_user(data_uptade: UserSchema, user_cod: int):
    #print (data_uptade)
    with engine.connect() as conn:
        #print (data_uptade)
        
        encrypt_pass = generate_password_hash(data_uptade.user_pass, "pbkdf2:sha256:30", 30)
        #print (encrypt_pass)
        conn.execute(users.update().values(user_pass=encrypt_pass, 
                                           user_rut=data_uptade.user_rut, 
                                           user_name=data_uptade.user_name, 
                                           user_last_name=data_uptade.user_last_name, 
                                           profile_cod=data_uptade.profile_cod).where(users.c.user_cod == user_cod))
        result = conn.execute(users.select().where(users.c.user_cod == user_cod)).first()
        conn.commit()
        #conn.commit()
        # print (result)
        return result
        
@user.delete('/api/user/{userd_cod}', status_code=HTTP_204_NO_CONTENT)
def delete_user(user_cod: int):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.user_cod == user_cod))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)