"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

mas = [randint(0, 9) for i in range(10)]
print(mas, '\nМаксимальное: ', max(mas, key=mas.count))
