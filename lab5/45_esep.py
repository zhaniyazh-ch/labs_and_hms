import datetime
import numpy as np
import pandas as pd
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        self._name = name.strip().title()
        if "@" not in email:
            raise ValueError("Email-да @ болуы керек")
        self._email = email.lower().strip()

    @classmethod
    def from_string(cls, data: str):
        parts = [p.strip() for p in data.split(',')]
        return cls(int(parts[0]), parts[1], parts[2])

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

    def __del__(self):
        print(f"User {self._name} deleted")

    def to_dict(self):
        return {"id": self._id, "name": self._name, "email": self._email}


class Product:
    def __init__(self, product_id: int, name: str, price: float, category: str):
        self.id = product_id
        self.name = name.strip().title()
        self.price = float(price)
        self.category = category.strip().capitalize()

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "category": self.category}


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, p: Product):
        if p.id not in [prod.id for prod in self.products]:
            self.products.append(p)

    def filter_by_price(self, min_p: float):
        f = lambda x: x.price >= min_p
        return [p for p in self.products if f(p)]


@app.get("/")
def welcome():
    return {"message": "Сервер қосулы. /docs арқылы тексеріңіз"}


@app.get("/task1-5")
def task_1_5():
    u = User(1, " alibi ", "Alibi@Example.kz")
    inv = Inventory()
    p1 = Product(101, " Smartphone ", 800, "electronics")
    p2 = Product(102, " Mouse ", 25, "electronics")
    inv.add_product(p1)
    inv.add_product(p2)

    expensive = inv.filter_by_price(100.0)
    return {
        "user": str(u),
        "expensive_products": [p.to_dict() for p in expensive]
    }


@app.get("/task11-13")
def task_11_13():
    prices = np.array([500.0, 1000.0, 1500.0, 2000.0])
    mean_v = np.mean(prices)
    median_v = np.median(prices)
    # Нормализация
    norm = (prices - np.min(prices)) / (np.max(prices) - np.min(prices))
    return {
        "mean": float(mean_v),
        "median": float(median_v),
        "normalized": norm.tolist()
    }


@app.get("/task21-22", response_class=HTMLResponse)
def task_21_22():
    # DataFrame құру
    users_data = [{"id": 1, "name": "Alibi", "email": "a@mail.kz"}, {"id": 2, "name": "Asel", "email": "as@mail.kz"}]
    df = pd.DataFrame(users_data)
    return df.to_html(classes="table table-striped")


@app.get("/task26-28")
def task_26_28():
    df = pd.DataFrame({
        "category": ["Tech", "Home", "Tech", "Tech"],
        "price": [1200, 300, 800, 1000]
    })
    mean_cat = df.groupby("category")["price"].mean().to_dict()
    count_cat = df.groupby("category").size().to_dict()
    return {
        "mean_by_category": mean_cat,
        "count_by_category": count_cat
    }

@app.get("/task29-30", response_class=HTMLResponse)
def task_29_30():
    # Деректер қоры (Входные данные)
    data = {
        "id": [1, 2, 3],
        "name": ["Laptop", "Mouse", "Monitor"],
        "price": [1200.0, 25.0, 450.0]
    }
    
    df = pd.DataFrame(data)
    df['discounted_price'] = df['price'] * 0.9
    df_sorted = df.sort_values(by='price', ascending=False)
    return f"""
    <h2>Задача 29: Жаңа баған (Скидка 10%) қосылды</h2>
    <h2>Задача 30: Баға бойынша кему ретімен сұрыпталды</h2>
    {df_sorted.to_html(index=False, classes="table table-bordered")}
    """
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=7008)