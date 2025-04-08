from pydantic import BaseModel

class CustomerUpdate(BaseModel):
    name: str
    email: str
