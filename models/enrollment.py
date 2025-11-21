from pydantic import BaseModel

class Enrollment(BaseModel):
    id: int
    student_id: int
    course_id: int
