🚀 Product Management REST API

A RESTful API built using FastAPI to manage product data loaded from a CSV file.
The API supports retrieving all products and fetching a single product by ID.

Deployed publicly using Render for automated testing and evaluation.

📌 Project Objective

Implement a RESTful API that:

Loads product data from a CSV file

Exposes product data through GET endpoints

Returns responses in exact expected JSON format

Is publicly deployed for automated testing

🏗 Architecture Overview
Client → HTTP GET → FastAPI → CSV Data (Loaded at Startup) → JSON Response

Tech Stack

FastAPI – Web framework

Uvicorn – ASGI server

Python 3.11

Render – Cloud deployment platform

📂 Project Structure
product_api/
│
├── main.py           # FastAPI application
├── products.csv      # Product data source
├── requirements.txt  # Dependencies
├── runtime.txt       # Python version specification
└── README.md

📄 CSV File Format

The CSV file must contain the following columns:

id,name,description
1,Apple iPhone 15,Latest Apple smartphone
2,Samsung Galaxy S24,Flagship Android phone
3,Sony WH-1000XM5,Noise cancelling headphones

Requirements:

Column names must be exactly: id,name,description

No extra spaces

ID must be unique integer

🌐 API Endpoints
🔹 GET All Products
GET /products

Example Response
[
  {
    "id": 1,
    "name": "Apple iPhone 15",
    "description": "Latest Apple smartphone"
  },
  {
    "id": 2,
    "name": "Samsung Galaxy S24",
    "description": "Flagship Android phone"
  }
]

🔹 GET Single Product by ID
GET /products/{id}

Example
GET /products/1

Response
{
  "id": 1,
  "name": "Apple iPhone 15",
  "description": "Latest Apple smartphone"
}

❌ Error Handling

If product ID does not exist:

{
  "detail": "Product not found"
}


Status Code: 404

🖥 Local Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/product_api.git
cd product_api

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Server
uvicorn main:app --reload


Server will run at:

http://127.0.0.1:8000

📘 Swagger API Documentation

Available at:

http://127.0.0.1:8000/docs


After deployment:

https://your-app-name.onrender.com/docs

☁ Deployment (Render)
Start Command
uvicorn main:app --host 0.0.0.0 --port 10000

Python Version (runtime.txt)
python-3.11.9

Public API URL
https://your-app-name.onrender.com/products

🧪 Testing Before Submission

Test All Products:

https://your-app-name.onrender.com/products


Test Single Product:

https://your-app-name.onrender.com/products/1

⚠️ Important Notes for Automated Evaluation

Must use GET method

Endpoint must be exactly /products

Endpoint must be exactly /products/{id}

Response must NOT be wrapped inside another object

ID must be integer

Must return 200 for valid requests

Must return 404 for invalid product ID

Must use deployed public URL (NOT localhost)

📈 Design Decisions

Data is loaded once during application startup

In-memory storage ensures fast response time

Clean RESTful endpoint design

Minimal dependencies for lightweight deployment

No database required (CSV-driven system)

🎯 Assessment Readiness Checklist

✔ CSV-based data loading
✔ RESTful design
✔ Proper HTTP status codes
✔ JSON responses
✔ Public cloud deployment
✔ Swagger documentation

👨‍💻 Author

Developed as part of a practical assessment for REST API implementation and cloud deployment.