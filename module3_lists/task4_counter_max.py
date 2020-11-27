"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

mas = [randint(0, 9) for i in range(10)]
print(mas, '\nМаксимальное: ', max(mas, key=mas.count))

a = [randint(0, 9) for i in range(10)]
max_index = 0
for i in a:
    if a.count(max_index) < a.count(i):
        max_index = a.index(i)
print(max_index)
