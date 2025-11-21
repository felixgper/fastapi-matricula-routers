from fastapi import APIRouter, HTTPException
from models.enrollment import Enrollment
from routers.students import list_student
from routers.courses import list_courses

router = APIRouter(prefix="/enrollments", 
                   tags=["Enrollments"],
                   responses= {404: {"message" : "No encontrado"}}
                   )

list_enrollments = []

@router.get("/")
async def get_enrollment():
    if not list_enrollments:
        raise HTTPException(status_code= 404, detail= "NO SE ENCONTRO CONTENIDO EN LA LISTA")
    return list_enrollments

@router.post("/")
async def post_enrollment(enrollment : Enrollment):
    existing_student = search_student(enrollment.student_id)
    if existing_student is None:
        raise HTTPException(status_code= 404, detail= "NO EXISTE EL ESTUDIANTE")
    
    if existing_student.active is False:
        raise HTTPException(status_code=400, detail="EL ESTUDIANTE ESTÁ INACTIVO")
    
    existing_course = search_courses(enrollment.course_id)
    if existing_course is None:
        raise HTTPException(status_code= 404, detail= "NO SE ENCONTRO CURSO")
    
    if existing_course.active is False:
        raise HTTPException(status_code=400, detail="EL CURSO ESTÁ INACTIVO")
    
    for e in list_enrollments:
        if e.student_id == enrollment.student_id  and e.course_id == enrollment.course_id:
            raise HTTPException(status_code= 409, detail= "MATRICULA YA EXISTE")
    
    list_enrollments.append(enrollment)
    return enrollment

def search_student(student_id: int):
    for student in list_student:
        if student.id == student_id:
            return student
    return None

def search_courses(course_id: int):
    for course in list_courses:
        if course.id == course_id:
            return course
    return None