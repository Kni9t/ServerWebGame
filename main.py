from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import Models
import DBcontroller
import JSend

app = FastAPI()
databaseController = DBcontroller.db_controller()

app.mount(
    "/web/assets",
    StaticFiles(directory="web/assets"),
    name="assets"
)

@app.get("/")
def home_page():
    return FileResponse("web/index.html")

@app.post("/api/v1/users/login")
def read_root():
    return { '1': 1 }

@app.post("/api/v1/users/signup")
def signup(user: Models.UserReg):
    response = {}
    try:
        newUser = dict(user)

        insertID = databaseController.write("users", newUser)
        receivedUser = databaseController.read("users", insertID)
        receivedUser["_id"] = str(receivedUser["_id"])

        print(receivedUser)

        response = JSend.CreateJSend("success", "user", receivedUser)
    except:
        print ("Error")
    
    return response