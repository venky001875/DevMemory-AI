from pydantic import BaseModel

class HealthResponse(BaseModel):
    """Response model for the health check endpoint.

    * ``status`` – a short status string (e.g., "healthy").
    * ``service`` – name of the service providing the health information.
    """
    status: str
    service: str
