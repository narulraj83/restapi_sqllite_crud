from sqlalchemy.orm import Session
from models import Employee
from schemas import EmployeeCreate, EmployeeUpdate

# Create a new employee
def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(**employee.model_dump())

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee

# Read all employees
def get_employees(db: Session):
    return db.query(Employee).all()

# Read a single employee by ID
def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

# Update an existing employee
def update_employee(db: Session, employee_id: int, employee: EmployeeUpdate):
    db_employee = get_employee(db, employee_id)

    if db_employee:
        for key, value in employee.model.dump().items():
            setattr(db_employee, key, value)

        db.commit()
        db.refresh(db_employee)

    return db_employee

# Delete an employee
def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)

    if db_employee:
        db.delete(db_employee)
        db.commit()

    return db_employee   
    