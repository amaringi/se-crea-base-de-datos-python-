from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.TablasSQL import Base
from app.api.routes.endpoints import rutas
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware


# Crear las tablas SQL desde las definiciones del modelo
Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI()

#configurar el protocolo CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redirigir la raíz al endpoint de la documentación de FastAPI
@app.get("/", include_in_schema=False)
def main():
    return RedirectResponse(url="/docs")

# Incluir las rutas definidas en el archivo de endpoints
app.include_router(rutas)
