#1 Удвоить числа в списке (map)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#2 Преобразовать строки в заглавные (map)
words = ["кот", "машина", "арбуз", "дом"]
result = list(map(lambda w: w.upper() + "!" if len(w) > 3 else w.upper(), words))
print(result)
