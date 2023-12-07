from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..schemas import schemas
import requests
from ..auth import oauth2

router = APIRouter(tags=['Recipe'], prefix='/recipe')

@router.get('/', status_code=status.HTTP_200_OK)
def get_all_recipes(token: str = Depends(oauth2.get_current_token)):
    url = 'http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/'
    response = requests.get(url, headers = {'Authorization': f'Bearer {token}'})
    return response.json()

@router.get('/{recipe_id}', status_code=status.HTTP_200_OK)
def get_recipe_by_id(recipe_id: int, token: str = Depends(oauth2.get_current_token)):
    url = f'http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/{recipe_id}'
    response = requests.get(url, headers = {'Authorization': f'Bearer {token}'})
    return response.json()

@router.get('/category/{category}', status_code=status.HTTP_200_OK)
def get_recipe_by_category(category: str, token: str = Depends(oauth2.get_current_token)):
    url = f'http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/category/{category}'
    response = requests.get(url, headers = {'Authorization': f'Bearer {token}'})
    return response.json()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_recipe(request: schemas.RecipeCreate, token: str = Depends(oauth2.get_current_token)):
    url = 'http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/'
    response = requests.post(url, headers = {'Authorization': f'Bearer {token}'}, json=request.model_dump())
    return response.json()

