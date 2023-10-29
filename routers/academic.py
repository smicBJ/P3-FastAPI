from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


# The student model
class Student(BaseModel):
    name: str
    grade: int
    gpa: float
    nehs: bool | None = False


students = [
    Student(name="Hudson Jones", grade=11, gpa=4.0),
    Student(name="Samuel Wu", grade=12, gpa=3.1),
    Student(name="Jonathan Fernandes", grade=12, gpa=3.0)
]


@router.get("/")
async def get_all_academics():
    return students


@router.post("/")
async def add_new_student(student: Student):
    students.append(student)
    return {"msg": "Student Added"}


@router.get("/{student_name}")
async def get_student_academic_record(student_name: str):
    for student in students:
        if student_name.lower() in student.name.lower():
            return student
    return {"msg": f"{student_name} was not found"}
