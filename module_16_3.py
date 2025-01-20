from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def user_req():
    return users

@app.post("/user/{usernsme}/{age}")
async def user_regist(username: str = Query(max_length=100, min_length=10, description="Enter username and age", example="username - NewUser, age - 22")):
    new_index = str(int(max(users, key=int)) + 1)
    users[new_index] = username
    return f"User {new_index} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def user_update(user_id: int = Path(description="Enter id_User", example="1"),
new_data: str = Query(max_length=100, min_length=10, description="Enter username and age", example="username - NewUser, age - 22")):
    users[user_id] = new_data
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def del_user(user_id: str = Path(description="Enter id_User", example="1")):
    users.pop(user_id)
    return f"User {user_id} has been deleted"

#= Path(min_length=16, max_length=100, description="Вставлять строчку с именем и возрастом", example="Имя: Ядвига, возраст: 66")