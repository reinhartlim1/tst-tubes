import requests
from fastapi import Depends
from ..auth import oauth2

def get_token():
    url = "https://tst-api-order-production.up.railway.app/login"
    data = {
        'username': 'admin10@gmail.com',
        'password': 'admin10'
    }
    response = requests.post(url, data=data)
    return response.json()['access_token']

def get_api_data(url: str):
    headers = {
    'Authorization': f'Bearer {get_token()}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

 