import pytest
from app import app
from inventory_data import inventory

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Inventory API Running"

def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_single_item(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Milk"

def test_get_missing_item(client):
    response = client.get("/inventory/999")
    assert response.status_code == 404

def test_add_inventory_item(client):
    new_item = {
        "name": "Eggs",
        "quantity": 12,
        "price": 4.99,
        "category": "Dairy"
    }

    response = client.post("/inventory", json=new_item)

    assert response.status_code == 201
    assert response.get_json()["name"] == "Eggs"

def test_update_inventory_item(client):
    update_data = {
        "quantity": 20
    }

    response = client.patch("/inventory/1", json=update_data)

    assert response.status_code == 200
    assert response.get_json()["quantity"] == 20

def test_delete_inventory_item(client):
    item = {
        "id": 99,
        "name": "Delete Test",
        "quantity": 1,
        "price": 1.99,
        "category": "Test"
    }

    inventory.append(item)

    response = client.delete("/inventory/99")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Item deleted successfully"