from fastapi import APIRouter, Response 

from schema.user_schema import UserSchema

from config.db import conn

from model.user import users

from werkzeug.security import generate_password_hash, check_password_hash #libreria para encriptar



user = APIRouter()

@user.get("/")
def root():
    return {"message": "Hi, I am Router from Router"}

@user.post("/api/user")
def create_user(data_user: UserSchema):
    new_user = data_user.dict()#Crea Diccionario de datos
    new_user["user_pass"] = generate_password_hash(data_user.user_pass, "pbkdf2:sha256:30", 30)
    conn.execute(users.insert().values(new_user)) #Inserta Datos
    conn.commit()#Guarda datos en la Tabla
    return "success"
    #print (data_user)
    #print (new_user)
