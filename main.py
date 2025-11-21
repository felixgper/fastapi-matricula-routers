from fastapi import FastAPI
from routers import courses, enrollments, students

app = FastAPI(title = "API AVANZADA CON ROUTERS")

app.include_router(courses.router)
app.include_router(students.router)
app.include_router(enrollments.router)