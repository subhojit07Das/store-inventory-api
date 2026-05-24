from fastapi import FastAPI
from db import get_connection

app = FastAPI()

@app.get("/products") # decorator in python
def get_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, price, stock FROM products;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": float(row[2]),
            "stock": row[3]
        })
    
    return products

@app.get("/products/low-stock")
def get_low_stock(threshold: int = 100):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, stock FROM products WHERE stock < %s", (threshold,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    products = []
    for row in rows:
        products.append({
            "name": row[0],
            "stock": row[1]
        })
    
    return products