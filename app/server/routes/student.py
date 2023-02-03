from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)

from server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()

@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "student addes successfully!")

@router.get("/", response_description="Students record has been fetched")
async def get_students():
    studentsRecord = await retrieve_students()
    if studentsRecord:
        return ResponseModel(studentsRecord, "Student records retrieved successfully")
    return ErrorResponseModel("An Error occured", 404, "Empty list returned")

@router.get("/{id}", response_description="Student record has been fetched")
async def get_student(id):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Student record found!")
    return ErrorResponseModel("An error occured", 404, "Student record does not exist")

@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)

    if update_student:
        return ResponseModel(
            "Student with ID: {} name update is successful".format(id),
            "Student name updated successfully",
        )
    return ErrorResponseModel(
        "An Error occurred", 
        404,
        "There was an error updating the student data",
    )

@router.delete("/{id}", response_description="The student record has been deleted")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)

    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), 
            "Student deteleted successfully",
        )
    return ErrorResponseModel("An error Occurred", 404, "Student with id {0} doesn't exist".format(id))