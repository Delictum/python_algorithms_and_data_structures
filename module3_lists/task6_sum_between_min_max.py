"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

mas = [randint(0, 9) for i in range(10)]

min_i = mas.index(min(mas))
max_i = mas.index(max(mas))

print(f'Позиция минимального: {min_i}. Максимального: {max_i}')
if min_i > max_i:
    min_i, max_i = max_i, min_i


print(mas)
s = 0
for i in range(min_i+1, max_i):
    s += mas[i]
print(s)
