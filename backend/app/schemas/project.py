from pydantic import BaseModel, constr
from typing import Optional

class ProjectCreate(BaseModel):
    """Schema for creating a new project.

    Attributes
    ----------
    name: str
        Human‑readable name of the project. Must contain at least one non‑whitespace character.
    path: str
        Filesystem path where the project resides. Must contain at least one non‑whitespace character.
    """
    name: constr(min_length=1, strip_whitespace=True)
    path: constr(min_length=1, strip_whitespace=True)

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
    """Schema for updating a project. All fields are optional so the client can
    send only the attributes they wish to change. When provided, each field must
    contain at least one non‑whitespace character.
    """
    name: Optional[constr(min_length=1, strip_whitespace=True)] = None
    path: Optional[constr(min_length=1, strip_whitespace=True)] = None
