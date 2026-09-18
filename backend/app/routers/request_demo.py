from fastapi import APIRouter
from ..schemas.request_demo import RequestDemo

router = APIRouter()

@router.post("/demo", response_model=RequestDemo)
def demo_endpoint(payload: RequestDemo):
    """Accept a RequestDemo JSON payload and echo it back.

    FastAPI will validate the incoming JSON against the RequestDemo Pydantic model.
    """
    return {"name": payload.name, "message": payload.message}
