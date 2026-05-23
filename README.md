# Inventory API Project

This project is a simple Flask inventory management API. It allows users to view, add, update, and delete inventory items. It also connects to the OpenFoodFacts API to search for food product information.

## Features

- View all inventory items
- View one inventory item by ID
- Add a new inventory item
- Update an existing inventory item
- Delete an inventory item
- Search OpenFoodFacts and add product information
- Use a CLI to interact with the API
- Tests using pytest

## Error Handling

The project includes error handling for:

- Invalid inventory IDs
- Missing request data
- Invalid numeric inputs in the CLI
- API connection failures
- Product searches that return no results

# Project Setup

## 1. Clone the Repository

```bash
git clone 
cd inventory_project
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```
## 3. Activate Virtual Environment

### Ubuntu / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Start Flask API Server

```bash
python app.py
```

The API will run on:

```txt
http://127.0.0.1:5000
```

---

## Run the CLI Frontend

Open a second terminal window.

Activate the virtual environment again:

```bash
source venv/bin/activate
```

Then run:

```bash
python cli.py
```

---

# Testing

This project uses pytest for route testing.

Run tests with:

```bash
pytest
```