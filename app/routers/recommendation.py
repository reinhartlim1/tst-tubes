from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..controller.recommendation import *

router = APIRouter(tags=['Recommendation'], prefix='/recommendation')

@router.get('/recipe/{product_id}', status_code=status.HTTP_200_OK)
async def get_recommendation(product_id: int):
    return 0

