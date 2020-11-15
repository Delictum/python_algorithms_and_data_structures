"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

n_row = 3
n_col = 2
matrix = [[randint(0, 9) for _ in range(n_col)] for _ in range(n_row)]
sum_col = {}

print('Полученная матрица')
for row in range(n_row):
    for col in range(n_col):
        print(matrix[row][col], end=" ")
    print()

for col in range(n_col):
    sum_col[col] = 0
    for row in range(n_row):
        sum_col[col] += matrix[row][col]

min_sum_col = min(sum_col, key=lambda x: sum_col[x])
print('Номер столбца с минимальными элементами: ', min_sum_col)

max_elem = matrix[0][min_sum_col]
for row in range(n_row):
    if max_elem < matrix[row][min_sum_col]:
        max_elem = matrix[row][min_sum_col]

print("Максимальный элемент среди минимальных значений столбца: ", max_elem)

