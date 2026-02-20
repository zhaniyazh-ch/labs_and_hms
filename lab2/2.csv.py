import csv
employees = []
with open("employees.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row = {k.lower(): v for k, v in row.items()}
        row["salary"] = int(row["salary"])
        employees.append(row)
total_salary = sum(emp["salary"] for emp in employees)
average_salary = total_salary / len(employees)
dept_salaries = {}
for emp in employees:
    dept = emp["department"]
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(emp["salary"])
dept_avg = {dept: sum(salaries) / len(salaries) for dept, salaries in dept_salaries.items()}
max_dept = max(dept_avg, key=dept_avg.get)
max_employee = max(employees, key=lambda e: e["salary"])
high_salary_employees = [emp for emp in employees if emp["salary"] > average_salary]
with open("high_salary.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "department", "salary"])
    writer.writeheader()
    writer.writerows(high_salary_employees)
print("Средняя зарплата:", average_salary)
print("Средняя зарплата по отделам:", dept_avg)
print("Отдел с самой высокой средней зарплатой:", max_dept)
print("Самый высокооплачиваемый сотрудник:", max_employee["name"], "-", max_employee["salary"])
print("Сотрудники выше средней:", [emp["name"] for emp in high_salary_employees])#2