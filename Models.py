from pydantic import BaseModel

class UserReg(BaseModel):
    name: str
    email: str
    password: str
    passwordConfirm: str
    
class UserLog(BaseModel):
    email: str
    password: str