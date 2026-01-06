from fastapi import APIRouter, HTTPException, status
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

@router.get("/users/{user_id}")
def get_user(user_id: str):
    try:
        user = collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return serialize_user(user)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID"
        )


@router.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    result = collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"message": "User updated"}


@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    result = collection.delete_one({"_id": ObjectId(user_id)})

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"message": "User deleted"}

