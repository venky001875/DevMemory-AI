# http_demo.py - Demonstrates basic HTTP methods in FastAPI

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/demo/http", tags=["HTTP Demo"])


class SimpleItem(BaseModel):
    name: str


@router.get("/")
async def demo_get():
    """GET demonstration – reads data"""
    return {"method": "GET", "message": "Reading data"}


@router.post("/")
async def demo_post(item: SimpleItem):
    """POST demonstration – creates data"""
    return {"method": "POST", "name": item.name, "message": "Data created"}


@router.put("/{item_id}")
async def demo_put(item_id: int, item: SimpleItem):
    """PUT demonstration – replaces/updates data"""
    return {"method": "PUT", "item_id": item_id, "name": item.name, "message": "Data updated"}


@router.patch("/{item_id}")
async def demo_patch(item_id: int, item: SimpleItem):
    """PATCH demonstration – partially updates data"""
    return {"method": "PATCH", "item_id": item_id, "name": item.name, "message": "Data partially updated"}


@router.delete("/{item_id}")
async def demo_delete(item_id: int):
    """DELETE demonstration – removes data"""
    return {"method": "DELETE", "item_id": item_id, "message": "Item deleted"}
