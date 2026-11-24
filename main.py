from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import crud

from database import engine, get_db
from schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API")

@app.get("/")
def home():
    return {"message": "Employee Management API is running"}

# Create a new employee
@app.post("/employees", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

# Read all employees
@app.get("/employees", response_model=list[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

# Read a single employee by ID
@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):

    employee = crud.get_employee(db, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.get_employees(db)

# Update an existing employee
@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    
    updated = crud.update_employee(db, employee_id, employee)

    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")