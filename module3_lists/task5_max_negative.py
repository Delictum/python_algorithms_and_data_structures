"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import randint

mas = [randint(-9, 9) for i in range(10)]
print(mas, '\nМаксимальное отрицательное:', max(filter(lambda x: x < 0, mas)))
