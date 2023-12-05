from .auth import get_api_data

def show_users_orders():
    url = 'https://tst-api-order-production.up.railway.app/orders/'
    return get_api_data(url)

def show_all_orders():
    url = 'https://tst-api-order-production.up.railway.app/orders/all'
    return get_api_data(url)

def show_order_by_id(order_id: int):
    url = f'https://tst-api-order-production.up.railway.app/orders/{order_id}'
    return get_api_data(url)