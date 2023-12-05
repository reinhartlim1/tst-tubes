from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..controller.recipe import *

router = APIRouter(tags=['Recipe'], prefix='/recipe')

@router.get('/', status_code=status.HTTP_200_OK)
def get_all_recipes():
    return show_all_recipes()