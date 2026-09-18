from fastapi import APIRouter, Depends, Header
from typing import Dict

router = APIRouter(prefix="/demo", tags=["dependency_demo"])


def get_app_info() -> Dict[str, str]:
    """Simple dependency that returns static application information.

    Returns
    -------
    dict
        A dictionary with ``service`` and ``version`` keys.
    """
    return {
        "service": "DevMemory AI Backend",
        "version": "0.1.0",
    }


@router.get("/dependency")
def dependency_endpoint(app_info: dict = Depends(get_app_info)):
    """Endpoint demonstrating FastAPI ``Depends`` injection.

    Parameters
    ----------
    app_info: dict
        Injected result from ``get_app_info``.
    """
    return {
        "message": "Dependency injection is working",
        "app_info": app_info,
    }
def get_project_header(x_project_name: str = Header(..., alias="X-Project-Name")) -> str:
    """Dependency that extracts the ``X-Project-Name`` header.

    Parameters
    ----------
    x_project_name: str
        The project name extracted from the ``X-Project-Name`` HTTP header.
    Returns
    -------
    str
        The received project name.
    """
    return x_project_name


@router.get("/header")
def header_endpoint(project_name: str = Depends(get_project_header)):
    """Endpoint demonstrating header extraction via dependency.

    Parameters
    ----------
    project_name: str
        The project name extracted from the ``X-Project-Name`` header.
    """
    return {"message": "Header received", "project_name": project_name}

@router.get("/query")
def query_endpoint(name: str):
    """Endpoint demonstrating required query parameter.

    Parameters
    ----------
    name: str
        Required query parameter.
    """
    return {"message": "Query parameter received", "name": name}
