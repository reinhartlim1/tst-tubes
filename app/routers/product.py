from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..controller.product import *

router = APIRouter(tags=['Product'], prefix='/product')

@router.get('/', status_code=status.HTTP_200_OK)
def get_all_products():
    return show_all_products()