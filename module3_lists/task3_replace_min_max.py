"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

mas = [random.randint(1, 9) for i in range(5)]

max_e = max(mas)
max_i = mas.index(max_e)

min_e = min(mas)
min_i = mas.index(min_e)

print('Исходный:', mas)
mas[min_i], mas[max_i] = mas[max_i], mas[min_i]
print('Итоговый:', mas)
