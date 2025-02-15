from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import DBcontroller

app = FastAPI()
databaseController = DBcontroller.db_controller()

app.mount(
    "/assets",
    StaticFiles(directory="assets"),
    name="assets"
)

class User(BaseModel):
    name: str
    email: str
    password: str

@app.get("/")
def home_page():
    return FileResponse("index.html")

@app.post("/api/v1/users/login")
def read_root():
    return { '1': 1 }

@app.post("/api/v1/users/signup")
def signup(user: User):
    buf = dict(user)
    databaseController.write("users", buf)
    return {
        "status" : "success",
        "data": {
            "user":
            {
                "user": "123",
                "email": "123",
                "pass": "123"
                }
        }
        }