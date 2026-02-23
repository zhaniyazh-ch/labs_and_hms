import csv
import json
transactions = []
with open("transactions.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["amount"] = int(row["amount"])
        transactions.append(row)
user_ops = {}
for t in transactions:
    user = t["user_id"]
    user_ops[user] = user_ops.get(user, 0) + 1
fraud_transactions = [t for t in transactions if t["amount"] > 500000]
fraud_users = {user for user, count in user_ops.items() if count > 3}
fraud_sum = sum(t["amount"] for t in fraud_transactions)
with open("fraud_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Подозрительных транзакций: {len(fraud_transactions)}\n")
    f.write(f"Подозрительных пользователей: {len(fraud_users)}\n")
    f.write(f"Список пользователей: {', '.join(fraud_users) if fraud_users else 'нет'}\n")
    f.write(f"Общая сумма подозрительных операций: {fraud_sum}\n")
with open("fraud_users.json", "w", encoding="utf-8") as f:
    json.dump(list(fraud_users), f, ensure_ascii=False, indent=2)
print("Подозрительные транзакции:", fraud_transactions)
print("Подозрительные пользователи:", fraud_users)
print("Общая сумма подозрительных операций:", fraud_sum)