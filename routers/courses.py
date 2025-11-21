from fastapi import APIRouter, HTTPException
from models import course

router = APIRouter(prefix= "/courses",
                   tags= ["courses"],
                   responses= {404: {"message" : "No encontrado"}}
                   )
    
list_courses = []

@router.get("/")
async def get_courses():
    if not list_courses:
        raise HTTPException(status_code= 404, detail= "LISTA VACIA")
    return list_courses

@router.get("/{id}")
async def get_courses(id: int):
    if search_id(id) is None:
        raise HTTPException(status_code= 404, detail= "TAREA NO ENCONTRADA")
    return search_id(id)

@router.post("/")
async def post_courses(course : course.Courses):
    existing = search_id(course.id)
    if existing is not None:
        raise HTTPException(status_code= 409, detail= "ID YA EXISTE")
    list_courses.append(course)
    return course

@router.put("/{id}")
async def put_courses(id: int, course : course.Courses):
    
    found = False
    
    for index, value in enumerate(list_courses):
        if value.id == id:
            list_courses[index] = course
            found = True
            return {"message": "ESTUDIANTE ACTUALIZADO", "actualizado": course}
        
    if not found:
        raise HTTPException(status_code= 404, detail= "NO SE PUDO ELIMINAR ESTUDIANTE")
    
@router.delete("/{id}")
async def delete_courses(id: int):
    
    found = False
    
    for index, value in enumerate(list_courses):
        if value.id == id:
            del list_courses[index]
            found = True
            return {"message": "ESTUDIANTE ACTUALIZADO"}
        
    if not found:
        raise HTTPException(status_code= 404, detail= "NO SE PUDO ELIMINAR ESTUDIANTE")


def search_id(id: int):
    for course in list_courses:
        if course.id == id:
            return course
    return None