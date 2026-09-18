from fastapi import FastAPI
from .core.config import settings
from .routers.health import router as health_router
from .routers.request_demo import router as demo_router
from .routers.projects import router as projects_router
from .routers.http_demo import router as http_demo_router

app = FastAPI(title=settings.app_name, version=settings.version)
app.include_router(health_router)
app.include_router(demo_router)
app.include_router(projects_router)
app.include_router(http_demo_router)
from .routers.dependency_demo import router as dependency_demo_router
app.include_router(dependency_demo_router)

@app.get("/")
def read_root():
    """Root endpoint returning a simple confirmation JSON."""
    return {"message": "DevMemory AI backend is running"}


