from fastapi import APIRouter
from ..schemas.health import HealthResponse

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
def health_check():
    """Health check endpoint returning basic status JSON."""
    return {"status": "healthy", "service": "DevMemory AI"}

