from flask import Flask, request
from inventory_data import inventory
from openfoodfacts import search_food_product

app = Flask(__name__)

def get_next_id():
    if len(inventory) == 0:
        return 1
    return max(item["id"] for item in inventory) + 1

def find_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None

@app.route("/")
def home():
    return {"message": "Inventory API Running"}

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return inventory, 200

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    item = find_item(item_id)

    if item is None:
        return {"error": "Item not found"}, 404

    return item, 200

@app.route("/inventory", methods=["POST"])
def add_inventory_item():
    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    if "name" not in data or "quantity" not in data or "price" not in data:
        return {"error": "Name, quantity, and price are required"}, 400

    new_item = {
        "id": get_next_id(),
        "name": data["name"],
        "quantity": data["quantity"],
        "price": data["price"],
        "category": data.get("category", "General")
    }

    inventory.append(new_item)

    return new_item, 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    item = find_item(item_id)

    if item is None:
        return {"error": "Item not found"}, 404

    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    item["name"] = data.get("name", item["name"])
    item["quantity"] = data.get("quantity", item["quantity"])
    item["price"] = data.get("price", item["price"])
    item["category"] = data.get("category", item["category"])

    return item, 200

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):
    item = find_item(item_id)

    if item is None:
        return {"error": "Item not found"}, 404

    inventory.remove(item)

    return {"message": "Item deleted successfully"}, 200

@app.route("/inventory/search", methods=["POST"])
def search_and_add_food():
    data = request.get_json()

    if not data or "name" not in data:
        return {"error": "Product name is required"}, 400

    food_data = search_food_product(data["name"])

    if food_data is None:
        return {"error": "Product not found from OpenFoodFacts"}, 404

    new_item = {
        "id": get_next_id(),
        "name": food_data["product_name"],
        "quantity": data.get("quantity", 1),
        "price": data.get("price", 0),
        "category": food_data["category"],
        "brand": food_data["brand"]
    }

    inventory.append(new_item)

    return new_item, 201

if __name__ == "__main__":
    app.run(debug=True)