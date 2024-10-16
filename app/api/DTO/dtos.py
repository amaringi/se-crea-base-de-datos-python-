from pydantic import BaseModel,Field
from datetime import datetime

#los DTOS son clases que establecen el modelo de tranferencia de dstos
class UsuarioDTOPeticiones(BaseModel):
    nombres:str
    fechaNacimiento:datetime
    ubicacion:str
    metaAhorro:float
    class Config:
        orm_mode=True

class UsuarioDTORespuestas(BaseModel):
    id:int
    nombres: str
    metaAorro:float
    class Config:
        orm_mode=True

class GastoDTOPeticiones(BaseModel):
    descripcion:str
    categoria:str
    valor:float
    fecha:datetime
    class Config:
        orm_mode=True

class GastosDOTORespuestas(BaseModel):
    descripcion:str
    categoria:str
    valor:float
    fecha:datetime
    class Config:
        orm_mode=True

class CategoriaDTOPeticiones(BaseModel):
    nombre:str
    descripcion:str
    fotoCategoria:str
    class Config:
        orm_mode=True

class CategoriaDTORespuestas(BaseModel):
    id:str
    nombre:str
    descripcion:str
    fotoCategoria:str
    class Config:
        orm_mode=True

class IngresoDTOPeticiones(BaseModel):
    valor:float
    categoria:str
    fecha:datetime
    class Config:
        orm_mode=True

class IngresoDTORespuestas(BaseModel):
    id:int
    valor:float
    categoria:str
    fecha:datetime
    class Config:
        orm_mode=True
