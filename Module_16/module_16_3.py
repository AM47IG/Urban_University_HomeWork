from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                  example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> dict:
    user_id = int(max(users, key=int)) + 1
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return {"message": f'User {user_id} is registered'}


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)],
                   username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                 example="UrbanUser")],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> dict:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return {"message": f'User {user_id} has been updated'}


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]) -> dict:
    users.pop(str(user_id))
    return {"message": f'User {user_id} has been deleted'}
