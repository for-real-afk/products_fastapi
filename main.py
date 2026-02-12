from fastapi import FastAPI, HTTPException
from typing import List
import csv

app = FastAPI(title="Product Management API")

products = []

# Load CSV at startup
@app.on_event("startup")
def load_products():
    global products
    with open("products.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        products = [
            {
                "id": int(row["id"]),
                "name": row["name"],
                "description": row["description"]
            }
            for row in reader
        ]

# GET ALL PRODUCTS
@app.get("/products")
def get_all_products():
    return products

# GET SINGLE PRODUCT
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
