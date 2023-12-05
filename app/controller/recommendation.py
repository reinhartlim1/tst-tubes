from .auth import get_api_data
from .recipe import *
from .product import *


def recipe_recommendation(product_id: int):
    recommended_recipes = []
    product = show_product_by_id(product_id)
    print(product)
    recipes = show_all_recipes()
    for recipe in recipes:
        splitted_inggredient = recipe['ingredients'].split(',')
        for ingredient in splitted_inggredient:
            replacer = {
                'teaspoons':'',
                'teaspoon':'',
                'tablespoons':'',
                'tablespoon':'',
                'cups':'',
                'cup':'',
                'pounds':'',
                'pound':'',
                'ounces':'',
                'ounce':'',
                'grams':'',
                'gram':'',
                'kilograms':'',
                'kilogram':'',
                'ml':'',
                'liters':'',
                'liter':'',
                'milliliters':'',
                'milliliter':'',
                'milligrams':'',
                'milligram':'',
                'slices':'',
                'slice':'',
                'packages':'',
                        }
            for k, v in replacer.items():
                ingredient = ingredient.replace(k, v)
                if product['product_name'] in ingredient:
                    recommended_recipes.append(recipe)
                    break
        if not recommended_recipes:
            recommended_recipes = 'No recipes found'
    return recommended_recipes