from fastapi import APIRouter, HTTPException
from models import student

router = APIRouter(prefix= "/students",
                   tags= ["students"],
                   responses= {404: {"message" : "No encontrado"}}
                   )

list_student = []

@router.get("/")
async def get_student():
    if not list_student:
        raise HTTPException(status_code= 404, detail= "LISTA VACIA")
    return list_student

@router.get("/{id}")
async def get_students(id: int):
    if search_id(id) is None:
        raise HTTPException(status_code= 404, detail= "TAREA NO ENCONTRADA")
    return search_id(id)

@router.post("/")
async def post_students(student : student.Students):
    existing = search_id(student.id)
    if existing is not None:
        raise HTTPException(status_code= 409, detail= "ID YA EXISTE")
    list_student.append(student)
    return student

@router.put("/{id}")
async def put_student(id: int, student : student.Students):
    
    found = False
    
    for index, value in enumerate(list_student):
        if value.id == id:
            list_student[index] = student
            found = True
            return {"message": "ESTUDIANTE ACTUALIZADO", "actualizado": student}
        
    if not found:
        raise HTTPException(status_code= 404, detail= "NO SE PUDO ELIMINAR ESTUDIANTE")
    
@router.delete("/{id}")
async def delete_student(id: int):
    
    found = False
    
    for index, value in enumerate(list_student):
        if value.id == id:
            del list_student[index]
            found = True
            return {"message": "ESTUDIANTE ACTUALIZADO"}
        
    if not found:
        raise HTTPException(status_code= 404, detail= "NO SE PUDO ELIMINAR ESTUDIANTE")


def search_id(id: int):
    for student in list_student:
        if student.id == id:
            return student
    return None