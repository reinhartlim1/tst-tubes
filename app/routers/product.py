from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..schemas import schemas
import requests
from ..auth import oauth2

router = APIRouter(tags=['Product'], prefix='/product')

@router.get('/', status_code=status.HTTP_200_OK)
def get_all_products(token: str = Depends(oauth2.get_current_token)):
    url = 'https://tst-api-order-production.up.railway.app/products'
    response = requests.get(url, headers = {'Authorization': f'Bearer {token}'})
    return response.json()

@router.get('/{product_id}', status_code=status.HTTP_200_OK)
def get_product_by_id(product_id: int, token: str = Depends(oauth2.get_current_token)):
    url = f'https://tst-api-order-production.up.railway.app/products/{product_id}'
    response = requests.get(url, headers = {'Authorization': f'Bearer {token}'})
    return response.json()

