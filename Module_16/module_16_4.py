from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)] = None
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")]
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def post_user(user: User) -> User:
    if users:
        user.id = max(map(lambda x: x.id, users)) + 1
    else:
        user.id = 1
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user: User) -> User:
    try:
        index = list(map(lambda x: x.id, users)).index(user.id)
        users[index] = user
        return user
    except (IndexError, ValueError):
        raise HTTPException(status_code=404, detail="User was not found")
    except TypeError:
        raise HTTPException(status_code=404, detail="User id is not specified")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    try:
        index = list(map(lambda x: x.id, users)).index(user_id)
        return users.pop(index)
    except ValueError:
        raise HTTPException(status_code=404, detail="User was not found")
