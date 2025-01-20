from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_pade():
    return "Вы вошли как администратор"

@app.get("/user/{item_id}")
async def user_id(item_id: int):
    return f"Вы вошли как пользователь № {item_id}"

@app.get("/user/")
async def user_page(username: str = "Noname", age: int = 0):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"