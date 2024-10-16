from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.DTO.dtos import UsuarioDTOPeticiones, UsuarioDTORespuestas, GastoDTOPeticiones,GastosDOTORespuestas, CategoriaDTOPeticiones, CategoriaDTORespuestas,IngresoDTOPeticiones,IngresoDTORespuestas
from app.api.models.TablasSQL import Usuario, Gasto, Categoria, Ingreso
from app.database.configuration import SessionLocal, engine

rutas=APIRouter()

def conectarConBd():
    try:
        baseDatos=SessionLocal()
        yield baseDatos

    except Exception as error:
        baseDatos.rollback()
        raise error

    finally:  
        baseDatos.close()

#construyendo nuestros servicios

#cada servicio (operacion o transaccioon en BD) deve programarse como una funcion
@rutas.post("/usuario", response_model=UsuarioDTORespuestas
            
            , summary="registrar un usuario en la base de datos")
def guardarUsuario(datosUsuario: UsuarioDTOPeticiones, dataBase: Session=Depends(conectarConBd)):
    try:
        usuario=Usuario(
            nombres=datosUsuario.nombres,
            fechaNacimiento=datosUsuario.fechaNacimiento,
            ubicacion=datosUsuario.ubicacion,
            metaAhorro=datosUsuario.metaAhorro
        )
        #ordenandole a la BD
        dataBase.add(usuario)
        dataBase.commit()
        dataBase.refresh(usuario)
        return {"mensaje":"Usuario guardado correctamente"}

    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")


@rutas.get("/usuario",response_model=List[UsuarioDTORespuestas],summary="buscar todos los usuarios en una base de datos")  
def buscarUsuario(datosUsuario: UsuarioDTOPeticiones, dataBase: Session=Depends(conectarConBd)):
    
    try:
        usuarios=dataBase.query(Usuario).all()
        return usuarios



    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")



#gastos

@rutas.post("/gasto", response_model=GastosDOTORespuestas, summary="registrar un usuario en la base de datos")
def guardarUsuario(datosGastos: GastoDTOPeticiones, dataBase: Session=Depends(conectarConBd)):
    try:
        gasto=Gasto(
            descripcion=datosGastos.descripcion,
            categoria=datosGastos.categoria,
            valor=datosGastos.valor,
            fecha=datosGastos.fecha,
        )
        #ordenandole a la BD
        dataBase.add(gasto)
        dataBase.commit()
        dataBase.refresh(gasto)
        return {"mensaje":"Usuario guardado correctamente"}

    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")


@rutas.get("/gasto",response_model=List[GastosDOTORespuestas],summary="buscar todos los usuarios en una base de datos")  
def buscarUsuario(datosGastos: GastoDTOPeticiones, dataBase: Session=Depends(conectarConBd)):
    
    try:
        gastos=dataBase.query(Usuario).all()
        return gastos



    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")

#categoria

@rutas.post("/categoria", response_model=CategoriaDTORespuestas, summary="registrar una categoria en la base de datos")
def guardarUsuario(datosCategorias: CategoriaDTOPeticiones, dataBase: Session=Depends(conectarConBd)):
    try:
        categoria=Categoria(
            nombre=datosCategorias.nombre,
            descripcion=datosCategorias.descripcion,
            fotoCategoria=datosCategorias.fotoCategoria,
        )
        #ordenandole a la BD
        dataBase.add(categoria)
        dataBase.commit()
        dataBase.refresh(categoria)
        return {"mensaje":"Usuario guardado correctamente"}
    
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")
    

@rutas.get("/categoria",response_model=List[CategoriaDTORespuestas],summary="buscar todas las categorias en una base de datos")  
def buscarUsuario(datosCategorias: CategoriaDTOPeticiones, dataBase: Session=Depends(conectarConBd)):
    
    try:
        categorias=dataBase.query(Usuario).all()
        return categorias
    
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")
    
#ingreso

@rutas.post("/ingreso", response_model=IngresoDTORespuestas, summary="registrar un ingreso en la base de datos")
def guardarUsuario(datosIngresos: IngresoDTOPeticiones, dataBase: Session=Depends(conectarConBd)):
    try:
        ingreso=Ingreso(
            descripcion=datosIngresos.descripcion,
            categoria=datosIngresos.categoria,
            valor=datosIngresos.valor,
            fecha=datosIngresos.fecha,
        )
        #ordenandole a la BD
        dataBase.add(ingreso)
        dataBase.commit()
        dataBase.refresh(ingreso)
        return {"mensaje":"Usuario guardado correctamente"}
    
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")
    

@rutas.get("/ingreso",response_model=List[IngresoDTORespuestas],summary="buscar todos los ingresos en una base de datos")  
def buscarUsuario(datosIngresos: IngresoDTOPeticiones, dataBase: Session=Depends(conectarConBd)):
    
    try:
        ingresos=dataBase.query(Usuario).all()
        return ingresos
    
    except Exception as error:
        dataBase.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")
    

    
    


