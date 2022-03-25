from bson import ObjectId
from fastapi import APIRouter

from config.database import connection
from models.students import Student
from schemas.students import list_of_student_entity, student_entity

router = APIRouter()


@router.get('')
async def find_all_students():
    return list_of_student_entity(connection.local.students.find())


@router.get('/{student_id}')
async def find_student_by_id(student_id: str):
    find_student = connection.local.students.find_one(
        {'_id': ObjectId(student_id)})
    return student_entity(find_student)


@router.post('')
async def create_student(student: Student):
    student = connection.local.students.insert_one(dict(student))
    return student_entity(connection.local.students.find_one({'_id': student.inserted_id}))


@router.put('/{student_id}')
async def update_student(student_id: str, student: Student):
    connection.local.students.find_one_and_update(
        {'_id': ObjectId(student_id)},
        {'$set': dict(student)})
    return student_entity(connection.local.students.find_one({'_id': ObjectId(student_id)}))


@router.delete('/{student_id}')
async def delete_student(student_id: str):
    del_student = connection.local.students.find_one_and_delete(
        {'_id': ObjectId(student_id)})
    return student_entity(del_student)
