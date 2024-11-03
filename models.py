from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
     
class Usuario(BaseModel):
    id: str 
    nombre: str
    email: str 
    edad: int 

class Proyecto(BaseModel):
    id: str 
    nombre: str 
    desripcion:str
    idusuario: str 