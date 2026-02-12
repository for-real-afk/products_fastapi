from fastapi import FastAPI, HTTPException
import csv

app = FastAPI(title="Product Management API")

products = []

@app.on_event("startup")
def load_products():
    global products
    products = []

    with open("products.csv", mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)  # ✅ default comma delimiter

        for row in reader:
            # Skip empty rows
            if not row.get("Id"):
                continue

            products.append({
                "id": int(row["Id"]),
                "name": row["Product Name"],
                "description": row["Description"]
            })


@app.get("/products")
def get_all_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")
