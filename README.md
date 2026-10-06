# Tradexa Django Assignment

## Project Overview

A Django REST Framework application for managing products, orders, and packaging boxes.

The application provides REST APIs to:

* Create and manage products
* Create and manage boxes
* Create orders containing multiple products
* Calculate suitable boxes for an order based on product dimensions and total weight

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* REST API

## Project Structure

```text
Tradexa_Django_Assignment/
│
├── config/
├── shipping/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

Clone the repository and navigate to the project directory.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## API Endpoints

### Products

```text
GET    /api/products/
POST   /api/products/
GET    /api/products/{id}/
PUT    /api/products/{id}/
PATCH  /api/products/{id}/
DELETE /api/products/{id}/
```

### Boxes

```text
GET    /api/boxes/
POST   /api/boxes/
GET    /api/boxes/{id}/
PUT    /api/boxes/{id}/
PATCH  /api/boxes/{id}/
DELETE /api/boxes/{id}/
```

### Orders

```text
GET    /api/orders/
POST   /api/orders/
GET    /api/orders/{id}/
PUT    /api/orders/{id}/
PATCH  /api/orders/{id}/
DELETE /api/orders/{id}/
```

### Calculate Suitable Boxes

```text
POST /api/orders/{id}/calculate-boxes/
```

This endpoint calculates the total order weight and identifies boxes whose maximum weight and dimensions can accommodate the products.

## Example Product

```json
{
    "name": "Laptop",
    "length": 30,
    "width": 20,
    "height": 5,
    "weight": 2
}
```

## Example Box

```json
{
    "name": "Small Box",
    "length": 40,
    "width": 30,
    "height": 20,
    "max_weight": 5
}
```

## Example Order

```json
{
    "products": [1, 2, 3]
}
```

## Example Calculation

```text
Laptop    → 30 × 20 × 5 → 2 kg
Keyboard  → 45 × 15 × 3 → 1 kg
Mouse     → 12 × 7 × 4   → 0.2 kg

Total weight = 3.2 kg
```

## Author

Jede Jagadeeswar
