from fastapi import FastAPI
from fastapi.responses import JSONResponse
import csv

app = FastAPI()

products = []


@app.on_event("startup")
def load_products():
    global products
    products = []

    with open("products.csv", mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not row.get("Id"):
                continue

            products.append({
                "id": int(row["Id"]),
                "name": row["Product Name"]
            })


# ✅ STATIC ROUTE FIRST (IMPORTANT)
@app.get("/products")
def get_all_products():
    return products


# ✅ DYNAMIC ROUTE AFTER
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return JSONResponse(
        status_code=404,
        content={"error": "Product not found"}
    )
