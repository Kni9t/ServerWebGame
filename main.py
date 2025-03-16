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
def signup(receivedUser: Models.UserReg):
    response = {}
    try:
        newUser = dict(receivedUser)
        
        # email, name, pass, passwordConfirm validation
        
        if (databaseController.find("users", "email", newUser["email"]) != None):
            return JSend.CreateJSend("fail", "signup", { "email" : "This email is already taken" })

        if (newUser["password"] != newUser["passwordConfirm"]):
            return JSend.CreateJSend("fail", "signup", { "password" : "Passwords don't match" })
                
        insertID = databaseController.write("users", newUser)
        gettingUser = databaseController.find("users", "_id", insertID)
        gettingUser["_id"] = str(gettingUser["_id"])
        print(gettingUser)

        response = JSend.CreateJSend("success", "signup", gettingUser)
    except Exception as e:
        response = JSend.CreateJSend("error", "signup", dict(receivedUser), e)
    
    return response

app.mount("/", StaticFiles(directory="web", html = True))

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.2", port=3000)