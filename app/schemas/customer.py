from pydantic import BaseModel, EmailStr

class CustomerUpdate(BaseModel):
    name: str
    email: EmailStr
    
    class Config:
        orm_mode = True
