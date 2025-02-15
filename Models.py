from pydantic import BaseModel

class UserReg(BaseModel):
    name: str
    email: str
    password: str

class UserLog(BaseModel):
    email: str
    password: str