from fastapi import FastAPI
from routes.api import router as students_router

app = FastAPI()

app.include_router(students_router, tags=['Students'], prefix='/students')
