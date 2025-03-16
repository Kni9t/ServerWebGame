from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

import Models
import DBcontroller
import JSend

app = FastAPI()

databaseController = DBcontroller.db_controller()

@app.post("/api/v1/users/login")
def checkLogin(receivedUser: Models.UserLog):
    receivedUser = dict(receivedUser)
    response = {}
    
    user = databaseController.find("users", "email", receivedUser["email"])
    if (user != None):
        user["_id"] = str(user["_id"])
        
        if (user["password"] == receivedUser["password"]):
            response = JSend.CreateJSend("success", "login", user)
        else:
            response = JSend.CreateJSend("error", "login", receivedUser, "Invalid password")
    else:
        response = JSend.CreateJSend("error", "login", receivedUser, "User not found in database")
    
    return response

@app.post("/api/v1/users/signup")
def signup(user: Models.UserReg):
    response = {}
    try:
        newUser = dict(user)

        # email, name, pass, passwordConfirm
        
        insertID = databaseController.write("users", newUser)
        receivedUser = databaseController.find("users", "_id", insertID)
        receivedUser["_id"] = str(receivedUser["_id"])
        print(receivedUser)

        response = JSend.CreateJSend("success", "user", receivedUser)
    except Exception as e:
        response = JSend.CreateJSend("error", "user", dict(user), e)
    
    return response

app.mount("/", StaticFiles(directory="web", html = True))

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.2", port=3000)