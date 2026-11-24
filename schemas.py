from pydantic import BaseModel, EmailStr, ConfigDict

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    department: str
    salary: float

class EmployeeUpdate(BaseModel):
    name: str
    email: EmailStr
    department: str
    salary: float

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    salary: float

    model_config = ConfigDict(from_attributes=True)
    
