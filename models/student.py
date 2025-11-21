from pydantic import BaseModel

class Students(BaseModel):
    id: int
    name: str
    age: int
    career: str
    active: bool
    