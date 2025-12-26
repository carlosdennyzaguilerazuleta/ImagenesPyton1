# main.py
from fastapi import FastAPI

from routers.auth_routes import router as auth_router
from routers.math_images import router as math_router

app = FastAPI(title="Math Image API")


@app.get("/")
def health_check():
    return {"status": "ok"}


# Rutas de auth (no llevan JWT)
app.include_router(auth_router)

# Rutas de imágenes (protegidas con JWT)
app.include_router(math_router, prefix="/api")
