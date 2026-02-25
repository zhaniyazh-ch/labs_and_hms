import string
def analyze_orders(orders):
    def has_digits(s):
        return any(ch.isdigit() for ch in s)
    def sum_digits(num):
        return sum(int(d) for d in str(int(num)) if d.isdigit())
    def is_palindrome(word):
        return word == word[::-1]
    vowels = set("aeiou")
    filtered_orders = []
    for order in orders:
        if not has_digits(order["customer"]):
            order["customer"] = order["customer"].title()
            filtered_orders.append(order)
    for order in filtered_orders:
        processed_items = []
        for item in order["items"]:
            price, qty = item["price"], item["quantity"]
            if price > 100 and qty > 1:
                price = price * qty
            if qty % 2 == 1:
                price += sum_digits(price)
            if price > 0:
                processed_items.append({"name": item["name"], "price": price, "quantity": qty})
        order["processed_items"] = processed_items
    all_words_per_order = []
    all_vowels = set()
    for order in filtered_orders:
        text = " ".join(order["notes"]).lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = set(text.split())
        valid_words = {w for w in words if len(w) >= 4 and not is_palindrome(w)}
        all_words_per_order.append(valid_words)
        for w in valid_words:
            all_vowels |= {ch for ch in w if ch in vowels}
        order["words"] = valid_words
    word_counts = {}
    for words in all_words_per_order:
        for w in words:
            word_counts[w] = word_counts.get(w, 0) + 1
    word_counts = {w: c for w, c in word_counts.items() if c >= 2}
    word_counts = dict(sorted(word_counts.items(), key=lambda x: (-x[1], x[0])))
    unique_products = set()
    for order in filtered_orders:
        for item in order["processed_items"]:
            unique_products.add(item["name"])
    orders_by_total = sorted(
        filtered_orders,
        key=lambda o: (-sum(i["price"] for i in o["processed_items"]), o["order_id"])
    )
    orders_by_total = [o["order_id"] for o in orders_by_total]
    orders_by_item_count = {}
    for order in filtered_orders:
        count = len(order["processed_items"])
        if count not in orders_by_item_count:
            orders_by_item_count[count] = []
        if order["order_id"] not in orders_by_item_count[count]:
            orders_by_item_count[count].append(order["order_id"])
    return {
        "orders": [{"order_id": o["order_id"], "customer": o["customer"], "processed_items": o["processed_items"]} for o in filtered_orders],
        "word_counts": word_counts,
        "all_vowels": all_vowels,
        "unique_products": unique_products,
        "orders_by_total": orders_by_total,
        "orders_by_item_count": orders_by_item_count
    }
orders_data = [
    {
        "order_id": "A123",
        "customer": "john_doe42",
        "items": [{"name": "Laptop", "price": 999.99, "quantity": 1}, {"name": "Mouse2", "price": 25, "quantity": 2}],
        "notes": ["Deliver ASAP", "fragile package", "handle with care"]
    },
    {
        "order_id": "B456",
        "customer": "Alice",
        "items": [{"name": "Phone", "price": 500, "quantity": 2}, {"name": "Case", "price": 20, "quantity": 1}],
        "notes": ["Handle carefully", "fragile package"]
    }
]
result_orders = analyze_orders(orders_data)
print("\nРезультат анализа заказов:")
print(result_orders)