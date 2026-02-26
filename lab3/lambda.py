#1 Определить тип числа
check = lambda x: "положительное" if x > 0 else ("отрицательное" if x < 0 else "ноль")
print(check(5))
print(check(-3))
print(check(0))

#2 Сортировка списка слов по длине и первой букве
words = ["арбуз", "кот", "машина", "дом", "ананас"]
sorted_words = sorted(words, key=lambda w: (len(w), w[0]))
print(sorted_words)

#3 Фильтр по условию
numbers = [5, 12, 7, 20, 33, 8]
result = list(filter(lambda x: x % 2 == 0 and x > 10, numbers))
print(result)

#4 Преобразование списка с условиями
numbers = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x**2 if x % 2 == 0 else x*3, numbers))
print(result)

#5 Лямбда с несколькими аргументами
compare = lambda a, b: "a больше" if a > b else ("b больше" if b > a else "равны")
print(compare(10, 7))
print(compare(3, 5))
print(compare(4, 4))