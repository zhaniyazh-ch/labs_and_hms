with open("shop_logs.txt", "r", encoding="utf-8") as file:
    unique_users = set()
    total_buys = 0
    total_sum = 0
    user_spending = {}
    for line in file:
        parts = line.strip().split(";")
        user_id = parts[1]
        action = parts[2]
        unique_users.add(user_id)
        if action == "BUY":
            total_buys += 1
            amount = int(parts[3])
            total_sum += amount
            user_spending[user_id] = user_spending.get(user_id, 0) + amount
max_user = ""
max_spent = 0
for user, spent in user_spending.items():
    if spent > max_spent:
        max_spent = spent
        max_user = user
average_check = total_sum / total_buys if total_buys > 0 else 0
with open("report.txt", "w", encoding="utf-8") as report:
    report.write("Уникальных пользователей: " + str(len(unique_users)) + "\n")
    report.write("Всего покупок: " + str(total_buys) + "\n")
    report.write("Общая сумма: " + str(total_sum) + "\n")
    report.write("Самый активный покупатель: " + max_user + "\n")
    report.write("Средний чек: " + str(average_check) + "\n")
print("Отчет успешно создан!")#1