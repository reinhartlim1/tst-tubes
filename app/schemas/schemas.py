from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config():
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class Order(BaseModel):
    product_id: int
    quantity: int

class RecipeBase(BaseModel):
    title: str
    level: str
    category: str
    ingredients: str
    directions: str
    published: bool = True

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config():
        from_attributes = True

class FoodContentBase(BaseModel):
    title: str
    desc: str
    topic: str
    published: bool = True

class ContentCreate(FoodContentBase):
    pass

class FoodContent(FoodContentBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut    

    class Config():
        from_attributes = True

class ReviewBase(BaseModel):
    rating: int
    review: str