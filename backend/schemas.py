
from pydantic import BaseModel,Field
from typing import Optional

class Product(BaseModel):
    id:int|None=None
    name:str
    category:str
    price:float = Field(gt=0,description="price must be greater than 0.0")
    stock:int=Field(ge=0,description="stoct must be 0 or more")

class ProductUpdate(BaseModel):
    price:Optional[float]=Field(default=None,gt=0,description="price must be greater than 0.0")
    stock:Optional[int]=Field(default=None,ge=0,description="stock must be 0 or more")

class Config:
    validate_assignment=True

