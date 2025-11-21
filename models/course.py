from pydantic import BaseModel

class Courses(BaseModel):
    id: int
    title: str
    credits: int
    teacher_id: int
    active: bool