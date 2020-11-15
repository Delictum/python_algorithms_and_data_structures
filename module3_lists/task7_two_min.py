"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

from random import randint

mas = [randint(0, 9) for i in range(10)]

if mas[0] > mas[1]:
    min_i1 = 0
    min_i2 = 1
else:
    min_i1 = 1
    min_i2 = 0

for i in range(2, len(mas)):
    if mas[i] < mas[min_i1]:
        b = min_i1
        min_i1 = i
        if mas[b] < mas[min_i2]:
            min_i2 = b
    elif mas[i] < mas[min_i2]:
        min_i2 = i

print(mas)
print(f'Минимальные: {mas[min_i1]} и {mas[min_i2]}')
