#1  Квадраты чётных чисел
squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares)

#2 Умножение всех чисел
matrix = [[1,2,3], [4,5,6], [7,8,9]]
result = [(lambda row: row[0] * row[1] * row[2])(r) for r in matrix]
print(result)

