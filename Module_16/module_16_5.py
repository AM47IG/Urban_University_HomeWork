from fastapi import FastAPI, Path, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)] = None
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")]
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]


@app.get("/")
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}")
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        user = users[list(map(lambda x: x.id, users)).index(user_id)]
    except ValueError:
        raise HTTPException(status_code=404, detail="User was not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


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
    except ValueError:
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
