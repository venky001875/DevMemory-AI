from pydantic import BaseModel
from typing import Optional
class ProjectCreate(BaseModel):
    """Schema for creating a new project.
    
    Attributes
    ----------
    name: str
        Human‑readable name of the project.
    path: str
        Filesystem path where the project resides.
    """
    name: str
    path: str

class ProjectResponse(BaseModel):
    """Schema returned to the client for a stored project.
    
    Attributes
    ----------
    id: int
        Unique identifier assigned by the temporary storage.
    name: str
        Project name.
    path: str
        Project filesystem path.
    """
    id: int
    name: str
    path: str
class ProjectUpdate(BaseModel):
    """Schema for updating a project. All fields are optional so the client can send
    only the attributes they wish to change.
    """
    name: Optional[str] = None
    path: Optional[str] = None

