from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pymongo
import json

app = FastAPI()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["webgame"]
collection = db["users"]

app.mount(
    "/assets",
    StaticFiles(directory="fastApiPy/assets"),
    name="assets"
)

@app.get("/")
def get_hello():
    return FileResponse("fastApiPy/index.html")

@app.post("/api/v1/users/login")
def read_root():
    return {collection.find_one()['name']}