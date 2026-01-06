from fastapi import APIRouter
from app.database import collection
from app.models import User
from bson import ObjectId

router = APIRouter()

def serialize_user(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"]
    }

# CREATE
@router.post("/users")
def create_user(user: User):
    result = collection.insert_one(user.dict())
    return {"message": "User created", "id": str(result.inserted_id)}

# READ ALL
@router.get("/users")
def get_users():
    users = collection.find()
    return [serialize_user(user) for user in users]

# READ ONE
@router.get("/users/{user_id}")
def get_user(user_id: str):
    user = collection.find_one({"_id": ObjectId(user_id)})
    return serialize_user(user)

# UPDATE
@router.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user.dict()}
    )
    return {"message": "User updated"}

# DELETE
@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    collection.delete_one({"_id": ObjectId(user_id)})
    return {"message": "User deleted"}
