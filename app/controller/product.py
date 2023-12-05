from .auth import get_api_data

def show_all_products():
    url = 'https://tst-api-order-production.up.railway.app/products'
    return get_api_data(url)

def show_product_by_id(product_id: int):
    url = f'https://tst-api-order-production.up.railway.app/products/{product_id}'
    return get_api_data(url)