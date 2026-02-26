#1 Чётные числа до n
def even_numbers(n):
    for i in range(2, n+1, 2):
        if i % 4 == 0:
            yield "кратно 4"
        else:
            yield i
for x in even_numbers(10):
    print(x)
