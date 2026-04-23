from fastapi import FastAPI
import pandas as pd
app = FastAPI()
def get_data():
    orders = pd.DataFrame({
        'order_id': [101, 102, 103, 104, 105],
        'user_id': [1, 2, 1, 3, 2],
        'product_name': ['Laptop', 'Mouse', 'Shirt', 'Monitor', 'T-Shirt'],
        'category': ['Electronics', 'Electronics', 'Clothing', 'Electronics', 'Clothing'],
        'price': [1200, 25, 500, 300, 20],
        'quantity': [1, 2, 1, 1, 3]
    })
    users = pd.DataFrame({
        'user_id': [1, 2, 3],
        'user_name': ['John', 'Alice', 'Bob']
    })
    orders['total_price'] = orders['price'] * orders['quantity']
    return orders, users
@app.get("/task31_32")
def task31_32():
    df, _ = get_data()
    return df.to_dict(orient="records")
@app.get("/task33")
def task33():
    df, _ = get_data()
    return df[df['category'] == "Electronics"].to_dict(orient="records")
@app.get("/task34")
def task34():
    df, _ = get_data()
    return df.groupby('category')['product_name'].count().reset_index(name='count').to_dict(orient="records")
@app.get("/task35")
def task35():
    df, _ = get_data()
    return df.groupby('category')['price'].mean().reset_index(name='mean_price').to_dict(orient="records")
@app.get("/task36")
def task36():
    df, _ = get_data()
    return df.sort_values(by='total_price', ascending=False).to_dict(orient="records")
@app.get("/task37")
def task37():
    df, _ = get_data()
    return df.nlargest(3, 'total_price').to_dict(orient="records")
@app.get("/task38")
def task38():
    df_o, df_u = get_data()
    return pd.merge(df_o, df_u, on='user_id').to_dict(orient="records")
@app.get("/final_report")
def final_report():
    df_o, df_u = get_data()
    merged = pd.merge(df_o, df_u, on='user_id')
    report = merged.groupby('user_name').agg(
        total_orders=('order_id', 'count'),
        total_sum=('total_price', 'sum'),
        mean_total=('total_price', 'mean'),
        max_order=('total_price', 'max'),
        unique_categories=('category', 'nunique')
    ).reset_index()
    report['VIP'] = report['total_sum'] > 1000
    report = report.sort_values(by=['total_sum', 'mean_total'], ascending=[False, True])
    return report.to_dict(orient="records")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)