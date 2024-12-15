from pydantic import BaseModel, ConfigDict

from datetime import datetime


class UserBase(BaseModel):
    first_name: str
    last_name: str
    father_name: str
    service_id: int
    birth_date: datetime
    
    
class UserCreate(UserBase):
    pass


class UserView(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int