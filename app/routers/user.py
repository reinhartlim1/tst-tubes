from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..schemas import schemas
from ..lib import utils
from ..models import models
import requests

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Email {user.email} already registered")
    order_url = "https://tst-api-order-production.up.railway.app/users/"
    order_response = requests.post(order_url, json=user.model_dump())
    data = {
        "email": user.email,
        "password": user.password,
    }
    recipe_url = "http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/users/"
    recipe_response = requests.post(recipe_url, json=data)
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)
    

    return new_user