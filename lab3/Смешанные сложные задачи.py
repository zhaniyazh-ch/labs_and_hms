#1 Генератор и фильтр по сложному условию
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def special_numbers(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        elif is_prime(i):
            yield "простое"
        else:
            yield i
for x in special_numbers(15):
    print(x)

#2 List comprehension + lambda + условия
words = ["кот", "машина", "арбуз", "дом", "ананас"]
result = [(lambda w: (w.upper() if len(w) > 4 else "short") + ("*" if "а" in w else ""))(w) for w in words]
print(result)

#3 Генератор + map + filter + условия
def process_numbers(numbers):
    for num in numbers:
        yield num
numbers = [5, -2, 8, 0, -7, 3]
filtered = filter(lambda x: x >= 0, process_numbers(numbers))
result = map(lambda x: x/2 if x % 2 == 0 else x*3 + 1, filtered)
for x in result:
    print(x)

#4 Dict comprehension + lambda + вложенные условия
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
grade_level = lambda score: "Отлично" if score >= 90 else ("Хорошо" if score >= 70 else "Удовлетворительно")
result = {name: grade_level(score) for name, score in students}
print(result)