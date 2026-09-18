from pydantic import BaseModel

class RequestDemo(BaseModel):
    """Demo request model used for a simple POST endpoint.

    * ``name`` – name of the caller (string)
    * ``message`` – an arbitrary message (string)
    """
    name: str
    message: str
