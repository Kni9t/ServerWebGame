from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException
import uvicorn, requests
import bcrypt
import jwt
from datetime import datetime, timedelta

import Models
from db_controller import DBController
import JSend

app = FastAPI()

databaseController = DBController("mongodb://localhost:27017/")

parametersDict = dict(databaseController.find('params')[0])
del parametersDict['_id']

@app.post("/api/v1/users/login")
def checkLogin(receivedUser: Models.UserLog):
    receivedUser = dict(receivedUser)
    response = {}
    
    user = databaseController.find("users", "email", receivedUser["email"])
    
    if (user != None):
        user["_id"] = str(user["_id"])
        
        if (bcrypt.checkpw(receivedUser["password"].encode(), user["password"])):
            user["password"] = user["password"].decode('utf-8')
            
            user['exp'] = str((datetime.now() + timedelta(days = 90)).strftime('%Y-%m-%d_%H:%M:%S'))
            
            token = jwt.encode(user, parametersDict['secret_key'], algorithm='HS256')
            
            response = JSend.CreateJSend("success", user)
            return JSONResponse(headers = {'Authorization': f'Bearer {token}'},status_code = 200, content = response)
        
    response = JSend.CreateJSend("fail", { "message" : "Invalid email or password" })
    return JSONResponse( status_code = 401, content = response)

@app.post("/api/v1/users/signup")
def signup(receivedUser: Models.UserReg):
    response = {}
    try:
        newUser = dict(receivedUser)
        
        # email, name, pass, passwordConfirm validation
        
        if (databaseController.find("users", "email", newUser["email"]) != None):
            return JSONResponse( status_code = 400, content = JSend.CreateJSend("fail", { "email" : "This email is already taken" }))

        if (newUser["password"] != newUser["passwordConfirm"]):
            return JSONResponse( status_code = 400, content = JSend.CreateJSend("fail", { "password" : "Passwords don't match" }))
        
        del newUser["passwordConfirm"]
        
        newUser["password"] = bcrypt.hashpw(newUser["password"].encode(), bcrypt.gensalt())
                
        insertID = databaseController.write("users", newUser)
        gettingUser = databaseController.find("users", "_id", insertID)
        gettingUser["_id"] = str(gettingUser["_id"])
        gettingUser["password"] = gettingUser["password"].decode()

        response = JSend.CreateJSend("success", gettingUser)
    except Exception as e:
        response = JSend.CreateJSend("error", dict(receivedUser), e)
        return JSONResponse( status_code = 500, content = response)    
    
    return JSONResponse( status_code = 200, content = response) 

@app.get("/api/v1/users")
def getAllUsers():
    response = {}
    
    users = databaseController.find("users")
    usersList = {}
    
    for user in users:
        user["_id"] = str(user["_id"])
        user["password"] = user["password"].decode()
        usersList[user["_id"]] = user
    
    response = JSend.CreateJSend("success", usersList)
    
    return JSONResponse( status_code = 200, content = response) 

app.mount("/", StaticFiles(directory="web", html = True))

@app.exception_handler(HTTPException)
def custom_http_exception_handler(request: requests, exc: HTTPException):    
    match exc.status_code:
        case 404:
            return JSONResponse(status_code = 404, content = JSend.CreateJSend("error", msg = "Page not found"))
        case 405:
            return JSONResponse(status_code = 405, content = JSend.CreateJSend("error", msg = "Method not allowed"))
        case _:
            return JSONResponse(status_code = exc.status_code, content = JSend.CreateJSend("error", msg = "Unsuspected error"))

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)