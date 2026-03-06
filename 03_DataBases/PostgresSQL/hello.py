from fastapi import FastAPI, Depends
from database import SessionLocal, engine
from models import Student, Base
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally: 
        db.close()


@app.post("/student")
def create_student(name: str, age: int, db: Session = Depends(get_db)):
    student = Student(name=name, age=age)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
