from fastapi import APIRouter, HTTPException, Response
from typing import List, Optional

from ..schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["projects"])

# Temporary in‑memory storage – will be replaced by PostgreSQL later.
# Using a dict keyed by integer IDs for O(1) lookup.
_projects: dict[int, ProjectResponse] = {}
_next_id: int = 1

@router.post("/", response_model=ProjectResponse)
def create_project(project: ProjectCreate):
    """Create a new project in temporary storage.

    Assigns an auto‑incrementing integer ID and stores the project.
    """
    global _next_id
    proj_resp = ProjectResponse(id=_next_id, name=project.name, path=project.path)
    _projects[_next_id] = proj_resp
    _next_id += 1
    return proj_resp

@router.get("/", response_model=List[ProjectResponse])
def get_all_projects():
    """Return a list of all stored projects."""
    return list(_projects.values())

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int):
    """Retrieve a single project by its ID.

    Raises:
        HTTPException: 404 if the project does not exist.
    """
    project = _projects.get(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
@router.patch("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, updates: ProjectUpdate):
    """Partially update a project.

    Only the fields supplied are changed; omitted fields stay unchanged.
    Returns the updated ProjectResponse.
    """
    existing = _projects.get(project_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Project not found")
    data = existing.dict()
    if updates.name is not None:
        data["name"] = updates.name
    if updates.path is not None:
        data["path"] = updates.path
    updated = ProjectResponse(**data)
    _projects[project_id] = updated
    return updated

@router.delete("/{project_id}", status_code=204)
def delete_project(project_id: int):
    """Delete a project.

    Returns HTTP 204 No Content on success.
    """
    if project_id not in _projects:
        raise HTTPException(status_code=404, detail="Project not found")
    del _projects[project_id]
    return Response(status_code=204)
