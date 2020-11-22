"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

from random import randint

# matrix = [[int(input()) for _ in range(5)] for _ in range(4)]
matrix = [[randint(0, 2) for _ in range(4)] for _ in range(4)]

for row in matrix:
    s = 0
    for cell in row:
        s += cell
        print(cell, end=" ")
    print('|', s)
