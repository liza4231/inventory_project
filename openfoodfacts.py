import requests

def search_food_product(product_name):
    url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": product_name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    products = data.get("products", [])

    if len(products) == 0:
        return None

    product = products[0]

    return {
        "product_name": product.get("product_name", product_name),
        "brand": product.get("brands", "Unknown"),
        "category": product.get("categories", "Unknown")
    }