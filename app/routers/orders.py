from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..controller.orders import *
from ..schemas import schemas
import requests
from ..controller.auth import get_token
from ..auth import oauth2

router = APIRouter(tags=['Orders'], prefix='/orders',dependencies=[Depends(oauth2.get_current_user)])

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all_orders():
    return show_all_orders()

@router.get('/', status_code=status.HTTP_200_OK)
async def get_users_orders():
    return show_users_orders()

@router.get('/{order_id}', status_code=status.HTTP_200_OK)
async def get_order_by_id(order_id: int):
    return show_order_by_id(order_id)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_order(request: schemas.Order):
    headers = {
    'Authorization': f'Bearer {get_token()}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }
    url = 'https://tst-api-order-production.up.railway.app/orders/'
    response = requests.post(url, headers = headers, json=request.model_dump())
    return response.json()
