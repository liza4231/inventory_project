import requests

BASE_URL = "http://127.0.0.1:5000"

def safe_request(method, url, **kwargs):
    try:
        response = method(url, **kwargs)
        print(response.json())
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure Flask is running.")
    except requests.exceptions.RequestException:
        print("Error: Something went wrong with the API request.")
    except ValueError:
        print("Error: Could not read the API response.")

def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return None

def get_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: Please enter a valid price.")
        return None

def show_menu():
    print("\nInventory CLI")
    print("1. View all inventory")
    print("2. View one item")
    print("3. Add item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Search OpenFoodFacts and add item")
    print("7. Exit")

def view_all():
    safe_request(requests.get, f"{BASE_URL}/inventory")

def view_one():
    item_id = get_int("Enter item ID: ")
    if item_id is None:
        return

    safe_request(requests.get, f"{BASE_URL}/inventory/{item_id}")

def add_item():
    name = input("Name: ")

    quantity = get_int("Quantity: ")
    if quantity is None:
        return

    price = get_float("Price: ")
    if price is None:
        return

    category = input("Category: ")

    data = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "category": category
    }

    safe_request(requests.post, f"{BASE_URL}/inventory", json=data)

def update_item():
    item_id = get_int("Enter item ID: ")
    if item_id is None:
        return

    quantity = get_int("New quantity: ")
    if quantity is None:
        return

    price = get_float("New price: ")
    if price is None:
        return

    data = {
        "quantity": quantity,
        "price": price
    }

    safe_request(requests.patch, f"{BASE_URL}/inventory/{item_id}", json=data)

def delete_item():
    item_id = get_int("Enter item ID: ")
    if item_id is None:
        return

    safe_request(requests.delete, f"{BASE_URL}/inventory/{item_id}")

def search_food():
    name = input("Food name to search: ")

    quantity = get_int("Quantity: ")
    if quantity is None:
        return

    price = get_float("Price: ")
    if price is None:
        return

    data = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    safe_request(requests.post, f"{BASE_URL}/inventory/search", json=data)

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            view_one()
        elif choice == "3":
            add_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            search_food()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 7.")

if __name__ == "__main__":
    main()