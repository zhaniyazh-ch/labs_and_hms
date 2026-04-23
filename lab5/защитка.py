import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
app = FastAPI(title="Pandas Tasks Server")
orders_data = {
    "order_id": [101, 103, 102],
    "user_name": ["John", "John", "Alice"],
    "total": [1200, 500, 25]
}
products_data = {
    "id": [1, 2, 3],
    "name": ["Laptop", "Mouse", "Monitor"],
    "category": ["Electronics", "Electronics", "Electronics"],
    "price": [1200.0, 25.0, 450.0]
}
@app.get("/")
def read_root():
    return {"message": "Pandas тапсырмалар сервері қосулы. /task26-28 немесе /task29-30 жолдарына өтіңіз."}
@app.get("/task26-28")
def task_26_28():
    df_orders = pd.DataFrame(orders_data)
    mean_total = df_orders.groupby("user_name")["total"].mean().to_dict() #26
    orders_count = df_orders.groupby("user_name").size().to_dict() #27
    df_prod = pd.DataFrame({
        "category": ["Electronics", "Electronics", "Clothing"],
        "price": [1200, 25, 20]
    })
    mean_price_cat = df_prod.groupby("category")["price"].mean().to_dict()
    return {
        "task26_mean_total": mean_total,
        "task27_orders_count": orders_count,
        "task28_mean_price_by_category": mean_price_cat
    } #28
@app.get("/task29-30", response_class=HTMLResponse)
def task_29_30():
    df = pd.DataFrame(products_data)
    df['discounted_price'] = df['price'] * 0.9 #29
    df_sorted = df.sort_values(by='price', ascending=False) #30
if _name_ == '_main_':
    uvicorn.run(app, host="127.0.0.1", port=7046)

