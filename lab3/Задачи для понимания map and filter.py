#1 Удвоить числа в списке (map)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#2 Преобразовать строки в заглавные (map)
words = ["кот", "машина", "арбуз", "дом"]
result = list(map(lambda w: w.upper() + "!" if len(w) > 3 else w.upper(), words))
print(result)

#3 Оставить только чётные числа (filter)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#4 Сложный фильтр с условиями (filter + map)
numbers = [0, 5, 12, 7, 20, -3, 8]
result = list(map(lambda x: x/2 if x % 2 == 0 else x*3,
                  filter(lambda x: x > 5, numbers)))
print(result)