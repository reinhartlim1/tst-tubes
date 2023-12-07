from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..schemas import schemas
import requests
from ..auth import oauth2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

router = APIRouter(tags=['Recommendation'], prefix='/recommendation')

@router.get('/recipe/{product_id}', status_code=status.HTTP_200_OK)
async def recipe_recommendation_based_on_product(product_id: int, token: str = Depends(oauth2.get_current_token)):
    recipe_recommendation = []
    # get product info
    url = f'https://tst-api-order-production.up.railway.app/products/{product_id}'
    product_response = requests.get(url, headers = {'Authorization': f'Bearer {token}'}).json()
    product_info = product_response['product_name']

    # get all recipe
    url = 'http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/'
    recipe_response = requests.get(url, headers = {'Authorization': f'Bearer {token}'}).json()
    if isinstance(recipe_response, list):
        selected_info = [{'title': recipe['title'], 'ingredients': recipe['ingredients']} for recipe in recipe_response]
        all_names = [product_info] + [recipe['title'] for recipe in selected_info]
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(all_names)
        similarity_matrix = cosine_similarity(vectors)
        product_index = 0
        similar_recipes_indices = similarity_matrix[product_index].argsort()[-4:-1][::-1]-1
        recipe_recommendation = [recipe_response[index] for index in similar_recipes_indices]
    else:
        print("Invalid response format.")
    return recipe_recommendation

@router.get('/recipe', status_code=status.HTTP_200_OK)
async def recipe_recommendation_based_on_order_history(token: str = Depends(oauth2.get_current_token)):
    recipe_recommendation = []
    # get all order history
    url = 'https://tst-api-order-production.up.railway.app/orders/'
    order_response = requests.get(url, headers = {'Authorization': f'Bearer {token}'}).json()
    if isinstance(order_response, list):
        ordered_products = [order['product_id'] for order in order_response]
        product_names = set()
        for product_id in ordered_products:
            product_url = f'https://tst-api-order-production.up.railway.app/products/{product_id}'
            product_response = requests.get(product_url, headers = {'Authorization': f'Bearer {token}'}).json()
            product_names.add(product_response['product_name'])
        product_names = list(product_names)
        recipe_url = 'http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe/'
        recipe_response = requests.get(recipe_url, headers = {'Authorization': f'Bearer {token}'}).json()
        if isinstance(recipe_response, list):
            selected_info = [{'title': recipe['title'], 'ingredients': recipe['ingredients']} for recipe in recipe_response]
            all_names = product_names + [recipe['title'] for recipe in selected_info]
            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform(all_names)
            similarity_matrix = cosine_similarity(vectors)
            product_index = len(product_names) - 1 
            similar_recipes_indices = similarity_matrix[product_index].argsort()[-5:-2][::-1]
            recipe_recommendation = [recipe_response[index] for index in similar_recipes_indices]
        else:
            print("Invalid response format.")
    
    else:
        print("Invalid response format.")
    return recipe_recommendation