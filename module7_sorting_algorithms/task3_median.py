"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима).
"""


"""В этой задаче как раз могла бы пригодиться быстрая сортировка Хоара или слиянием.
"Но без них не знаю, как можно написать более менее оптимизировано"""

import random

m = random.randint(5, 10)
# "одномерный вещественный массив, заданный случайными числами на промежутке [0; 50)" - т.е. [0; 49].
# Не знаю, важно ли это. uniform включает последнее число, в отличии от range и большинства прочих функций
# Для лучшей читабельности добавил округление
mas = [round(random.uniform(0, 49), 3) for i in range(2 * m + 1)]
print(f'Исходный список: {mas}')


# Через сортировку кучей
def heapify(array, size, ind):
    largest = ind
    left = (2 * ind) + 1
    right = (2 * ind) + 2

    if left < size and array[left] > array[largest]:
        largest = left

    if right < size and array[right] > array[largest]:
        largest = right

    if largest != ind:
        array[ind], array[largest] = array[largest], array[ind]
        heapify(array, size, largest)


def heap_sort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


heap_sort(mas)
print(f'Отсортированный список по возрастанию: {mas}')
print(f'Медиана: {mas[len(mas) // 2]}')


# Читерский вариант :)
import statistics

print(statistics.median(mas))
