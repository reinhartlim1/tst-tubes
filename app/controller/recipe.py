from .auth import get_api_data

def show_all_recipes():
    url = 'http://recipe-it.cxhpffgzgkhabfav.eastus.azurecontainer.io/recipe'
    return get_api_data(url)