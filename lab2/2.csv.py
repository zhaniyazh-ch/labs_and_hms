import csv
with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "department", "salary"])
    writer.writerow(["Ali", "IT", 500000])
    writer.writerow(["Dana", "HR", 300000])
    writer.writerow(["Arman", "IT", 600000])
    writer.writerow(["Aruzhan", "Marketing", 400000])
    writer.writerow(["Dias", "IT", 450000])
print("Файл employees.csv создан.")
employees = []
with open("employees.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)
avg_salary = sum(emp["salary"] for emp in employees) / len(employees)
departments = {}
for emp in employees:
    dept = emp["department"]
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(emp["salary"])
avg_by_dept = {dept: sum(salaries)/len(salaries) for dept, salaries in departments.items()}
best_dept = max(avg_by_dept, key=avg_by_dept.get)
top_employee = max(employees, key=lambda e: e["salary"])
above_avg = [emp for emp in employees if emp["salary"] > avg_salary]
with open("high_salary.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "department", "salary"])
    writer.writeheader()
    writer.writerows(above_avg)
print("Средняя зарплата:", avg_salary)
print("Средняя зарплата по отделам:", avg_by_dept)
print("Отдел с самой высокой средней зарплатой:", best_dept)
print("Самый высокооплачиваемый сотрудник:", top_employee["name"], "-", top_employee["salary"])
print("Сотрудники выше средней:", [emp["name"] for emp in above_avg])