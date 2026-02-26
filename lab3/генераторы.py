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

#3 Бесконечная последовательность
def infinite_numbers():
    i = 1
    while True:
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield i
        i += 1
gen = infinite_numbers()
for _ in range(15):
    print(next(gen))
