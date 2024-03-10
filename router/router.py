from fastapi import APIRouter 
from schema.user_schema import UserSchema

user = APIRouter()

@user.get("/")
def root():
    return {"message": "Hi, I am Router from Router"}

@user.post("/api/user")
def create_user(data_user: UserSchema):
    new_user = data_user.dict()#Crea Diccionario de datos
    print (data_user)
    print (new_user)
