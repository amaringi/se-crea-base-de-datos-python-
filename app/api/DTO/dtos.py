from pydantic import BaseModel, Field
from datetime import datetime


class LoginDTOPeticiones(BaseModel):
    correo: str
    contrasena: str
    nombres: str
    class Config:
        orm_mode = True

class LoginDTORespuestas(BaseModel):
    id: int
    correo: str
    contrasena: str
    nombres: str
    class Config:
        orm_mode = True

class RegistroDTOPeticiones(BaseModel):
    nombres: str
    correo: str
    contrasena: str
    class Config:
        orm_mode = True

class RegistroDTORespuestas(BaseModel):
    id: int
    correo: str
    contrasena: str
    nombres: str
    class Config:
        orm_mode = True

class UsuarioDTOPeticiones(BaseModel):
    nombres: str
    fechaNacimiento: datetime
    ubicacion: str
    metaAhorro: float

    class Config:
        orm_mode = True

class UsuarioDTORespuestas(BaseModel):
    id: int
    nombres: str
    metaAhorro: float
    class Config:
        orm_mode = True

class GastoDTOPeticiones(BaseModel):
    descripcion: str
    categoria: str
    valor: float
    fecha: datetime

    class Config:
        orm_mode = True

class GastoDTORespuestas(BaseModel):
    id: int
    descripcion: str
    categoria: str
    valor: float

    class Config:
        orm_mode = True

class CategoriaDTOPeticiones(BaseModel):
    nombre: str
    descripcion: str
    fotoCategoria: str
    fecha: datetime


    class Config:
        orm_mode = True

class CategoriaDTORespuestas(BaseModel):
    id: int
    nombre: str
    descripcion: str
    fotoCategoria: str

    class Config:
        orm_mode = True

class IngresoDTOPeticiones(BaseModel):
    valor: float
    descripcion: str
    fecha: datetime

    class Config:
        orm_mode = True

class IngresoDTORespuestas(BaseModel):
    id: int
    valor: float
    descripcion: str
    fecha: datetime

    class Config:
        orm_mode = True
