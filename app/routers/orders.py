from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..schemas import schemas
import requests
from ..auth import oauth2

router = APIRouter(tags=['Orders'], prefix='/orders')

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all_orders(token: str = Depends(oauth2.get_current_token)):
    url = 'https://tst-api-order-production.up.railway.app/orders/all'
    response = requests.get(url, headers = {'Authorization': f'Bearer {token}'})
    return response.json()

@router.get('/', status_code=status.HTTP_200_OK)
async def get_users_orders(token: str = Depends(oauth2.get_current_token)):
    url = 'https://tst-api-order-production.up.railway.app/orders/'
    response = requests.get(url, headers = {'Authorization': f'Bearer {token}'})
    return response.json()

@router.get('/{order_id}', status_code=status.HTTP_200_OK)
async def get_order_by_id(order_id: int, token: str = Depends(oauth2.get_current_token)):
    url = f'https://tst-api-order-production.up.railway.app/orders/{order_id}'
    response = requests.get(url, headers = {'Authorization': f'Bearer {token}'})
    return response.json()

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_order(request: schemas.Order, token: str = Depends(oauth2.get_current_token)):
    headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }
    url = 'https://tst-api-order-production.up.railway.app/orders/'
    response = requests.post(url, headers = headers, json=request.model_dump())
    return response.json()
