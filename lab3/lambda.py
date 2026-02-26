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