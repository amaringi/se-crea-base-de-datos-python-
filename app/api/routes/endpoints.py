from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.DTO.dtos import (UsuarioDTOPeticiones, UsuarioDTORespuestas, 
                              GastoDTOPeticiones, GastoDTORespuestas, 
                              CategoriaDTOPeticiones, CategoriaDTORespuestas, 
                              IngresoDTOPeticiones, IngresoDTORespuestas)

from app.api.models.TablasSQL import Usuario, Gasto, Categoria, Ingreso
from app.database.configuration import SessionLocal

rutas = APIRouter()

# Función para conectarse con la base de datos
def conectarConBd():
    try:
        baseDatos = SessionLocal()
        yield baseDatos
    except Exception as error:
        baseDatos.rollback()
        raise error
    finally:
        baseDatos.close()

# Servicio para registrar usuario
@rutas.post("/usuario", response_model=UsuarioDTORespuestas, summary="Registrar un usuario en la base de datos")
def guardarUsuario(datosUsuario: UsuarioDTOPeticiones, dataBase: Session = Depends(conectarConBd)):
    try:
        usuario = Usuario(
            nombres=datosUsuario.nombres,
            fechaNacimiento=datosUsuario.fechaNacimiento,
            ubicacion=datosUsuario.ubicacion,
            metaAhorro=datosUsuario.metaAhorro
        )
        dataBase.add(usuario)
        dataBase.commit()
        dataBase.refresh(usuario)
        return usuario  # Retornar el modelo `UsuarioDTORespuestas`
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema: {error}")

# Servicio para buscar todos los usuarios
@rutas.get("/usuario", response_model=List[UsuarioDTORespuestas], summary="Buscar todos los usuarios en la base de datos")
def buscarUsuarios(dataBase: Session = Depends(conectarConBd)):
    try:
        usuarios = dataBase.query(Usuario).all()
        return usuarios
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema: {error}")

# Servicio para registrar un gasto
@rutas.post("/gasto", response_model=GastoDTORespuestas, summary="Registrar un gasto en la base de datos")
def guardarGasto(datosGastos: GastoDTOPeticiones, dataBase: Session = Depends(conectarConBd)):
    try:
        gasto = Gasto(
            descripcion=datosGastos.descripcion,
            categoria=datosGastos.categoria,
            valor=datosGastos.valor,
            fecha=datosGastos.fecha,
        )
        dataBase.add(gasto)
        dataBase.commit()
        dataBase.refresh(gasto)
        return gasto  # Retornar el modelo `GastoDTORespuestas`
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema: {error}")

# Servicio para buscar todos los gastos
@rutas.get("/gasto", response_model=List[GastoDTORespuestas], summary="Buscar todos los gastos en la base de datos")
def buscarGastos(dataBase: Session = Depends(conectarConBd)):
    try:
        gastos = dataBase.query(Gasto).all()
        return gastos
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema: {error}")

# Servicio para registrar una categoría
@rutas.post("/categoria", response_model=CategoriaDTORespuestas, summary="Registrar una categoría en la base de datos")
def guardarCategoria(datosCategorias: CategoriaDTOPeticiones, dataBase: Session = Depends(conectarConBd)):
    try:
        categoria = Categoria(
            nombre=datosCategorias.nombre,
            descripcion=datosCategorias.descripcion,
            fotoCategoria=datosCategorias.fotoCategoria,
        )
        dataBase.add(categoria)
        dataBase.commit()
        dataBase.refresh(categoria)
        return categoria  # Retornar el modelo `CategoriaDTORespuestas`
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema: {error}")

# Servicio para buscar todas las categorías
@rutas.get("/categoria", response_model=List[CategoriaDTORespuestas], summary="Buscar todas las categorías en la base de datos")
def buscarCategorias(dataBase: Session = Depends(conectarConBd)):
    try:
        categorias = dataBase.query(Categoria).all()
        return categorias
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema: {error}")

# Servicio para registrar un ingreso
@rutas.post("/ingreso", response_model=IngresoDTORespuestas, summary="Registrar un ingreso en la base de datos")
def guardarIngreso(datosIngresos: IngresoDTOPeticiones, dataBase: Session = Depends(conectarConBd)):
    try:
        ingreso = Ingreso(
            valor=datosIngresos.valor,
            descripcion=datosIngresos.descripcion,
            fecha=datosIngresos.fecha,
        )
        dataBase.add(ingreso)
        dataBase.commit()
        dataBase.refresh(ingreso)
        return ingreso  # Retornar el modelo `IngresoDTORespuestas`
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema: {error}")

# Servicio para buscar todos los ingresos
@rutas.get("/ingreso", response_model=List[IngresoDTORespuestas], summary="Buscar todos los ingresos en la base de datos")
def buscarIngresos(dataBase: Session = Depends(conectarConBd)):
    try:
        ingresos = dataBase.query(Ingreso).all()
        return ingresos
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema: {error}")
