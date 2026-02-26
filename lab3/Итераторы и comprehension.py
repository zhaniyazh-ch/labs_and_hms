#1  Квадраты чётных чисел
squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares)

#2 Умножение всех чисел
matrix = [[1,2,3], [4,5,6], [7,8,9]]
result = [(lambda row: row[0] * row[1] * row[2])(r) for r in matrix]
print(result)

#3 Фильтр строк
words = ["кот", "машина", "ананас", "дом"]
filtered = [w for w in words if len(w) > 4 and "а" not in w]
print(filtered)

#4 Словарь с условиями
numbers = [1,2,3,4,5]
result = {n: ("чётное" if n % 2 == 0 else "нечётное") for n in numbers}
print(result)

#5 Flatten списка списков
matrix = [[1,2], [3,4], [5,6]]
flatten = [x for row in matrix for x in row]
print(flatten)

