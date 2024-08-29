from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    phone: str
    budget: float

@app.post("/post_add_users/")
async def add_user(user: User):
    # Gelen verileri kullanarak belirli bir işlem yapabilirsiniz.
    # Örneğin, bu verileri bir veritabanına kaydetmek için kullanabilirsiniz.
    return {"message": "Kullanıcı başarıyla eklendi", "user": user}
