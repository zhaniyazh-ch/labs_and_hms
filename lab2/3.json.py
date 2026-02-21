import json
from collections import Counter
with open("orders.json", encoding="utf-8") as f:
    orders = json.load(f)
total_revenue = sum(order["total"] for order in orders)
orders_by_user = {}
for order in orders:
    user = order["user"]
    orders_by_user[user] = orders_by_user.get(user, 0) + 1
total_items = sum(len(order["items"]) for order in orders)
top_order = max(orders, key=lambda o: o["total"])
top_user = top_order["user"]
all_items = [item for order in orders for item in order["items"]]
most_popular_item = Counter(all_items).most_common(1)[0][0]
summary = {
    "total_revenue": total_revenue,
    "top_user": top_user,
    "most_popular_item": most_popular_item,
    "total_orders": len(orders)
}
with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print("Общая сумма:", total_revenue)
print("Заказы по пользователям:", orders_by_user)
print("Всего товаров:", total_items)
print("Самый дорогой заказ у:", top_user)
print("Самый популярный товар:", most_popular_item)