from fastapi import APIRouter 
from config.database import collection_name
from models.todos_model import Todo 
from schemas.todos_schema import todo_serializer,todos_serializer
from bson import ObjectId

todo_api_router=APIRouter()

#retrieve
@todo_api_router.get("/")
async def get_todos():
    todos=todos_serializer(collection_name.find())
    return {"status":"ok","data":todos}

@todo_api_router.get("/{id}")

async def get_todo(id:str):
    todo=todos_serializer(collection_name.find({"_id":ObjectId(id)}))
    return {"status":"ok","data":todo}

#post

@todo_api_router.post("/")
async def post_todo(todo:Todo):
    _id=collection_name.insert_one(dict(todo))
    todo=todos_serializer(collection_name.find({"_id":_id.inserted_id}))  
    return {"status":"ok","data":todo}

#update todo
@todo_api_router.put("/{id}")
async def update_todo(id:str,todo:Todo):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(todo)
    })
    todo=todos_serializer(collection_name.find({"_id":ObjectId(id)}))
    return {"status":"ok","data":todo}
@todo_api_router.delete("/{id}")
async def delete_todo(id:str,todo:Todo):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
    return {"status":"ok","data":[]}