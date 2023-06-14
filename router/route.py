

from pymongo.mongo_client import MongoClient
from fastapi import APIRouter, Request, Response
from slowapi import Limiter
from slowapi.util import get_remote_address
from bson import ObjectId

from models import TodoBase
from schemas import list_serial, invidual_serial


client = MongoClient(
    "localhost",
    27017,
)

limiter = Limiter(
    key_func=get_remote_address
)

router = APIRouter(
    prefix="/api/v1",
)

db = client["todos"]

todos = db["todos"]

@router.get("/todos/{id}")
@limiter.limit("10/minute")
async def get_todo_by_id(request: Request, response: Response, id: str):
    todo = todos.find_one({"_id": ObjectId(id)})
    if todo is None:
        response.status_code = 404
        return {"message": "Todo not found"}
    return invidual_serial(todo)

@router.post("/todos")
@limiter.limit("10/minute")
async def create_new_todo(request: Request, response: Response, todo: TodoBase):
    todo = todos.insert_one(todo.dict())
    return {"id": str(todo.inserted_id)}

@router.put("/todos/{id}")
@limiter.limit("10/minute")
async def update_todo_by_id(request: Request, response: Response, id: str, todo: TodoBase):
    todo = todos.find_one_and_update({"_id": ObjectId(id)}, {"$set": todo.dict()})
    if todo is None:
        response.status_code = 404
        return {"message": "Todo not found"}
    return invidual_serial(todo)


@router.delete("/todos/{id}")
@limiter.limit("10/minute")
async def delete_todo_by_id(request: Request, response: Response, id: str):
    todo = todos.find_one_and_delete({"_id": ObjectId(id)})
    if todo is None:
        response.status_code = 404
        return {"message": "Todo not found"}
    return invidual_serial(todo)

@router.patch("/todos/{id}")
@limiter.limit("10/minute")
async def patch_todo_by_id(request: Request, response: Response, id: str, todo: TodoBase):
    todo = todos.find_one_and_update({"_id": ObjectId(id)}, {"$set": todo.dict()})
    if todo is None:
        response.status_code = 404
        return {"message": "Todo not found"}
    return invidual_serial(todo)
