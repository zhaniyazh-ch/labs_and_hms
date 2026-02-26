#1 Чётные числа до n
def even_numbers(n):
    for i in range(2, n+1, 2):
        if i % 4 == 0:
            yield "кратно 4"
        else:
            yield i
for x in even_numbers(10):
    print(x)

#2 Фильтрация строк
def filter_words(words):
    for w in words:
        if len(w) > 4:
            if "а" in w:
                yield "с а"
            else:
                yield w
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)
