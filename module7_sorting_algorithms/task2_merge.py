"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


size = 10
# "одномерный вещественный массив, заданный случайными числами на промежутке [0; 50)" - т.е. [0; 49].
# Не знаю, важно ли это. uniform включает последнее число, в отличии от range и большинства прочих функций
# Для лучшей читабельности добавил округление
mas = [round(random.uniform(0, 49), 3) for i in range(size)]
print(f'Исходный список: {mas}')


def merge(left, right):
    sorted_list = []
    left_ind = right_list_index = 0

    left_len, right_len = len(left), len(right)

    for _ in range(left_len + right_len):
        if left_ind < left_len and right_list_index < right_len:
            if left[left_ind] <= right[right_list_index]:
                sorted_list.append(left[left_ind])
                left_ind += 1
            else:
                sorted_list.append(right[right_list_index])
                right_list_index += 1

        elif left_ind == left_len:
            sorted_list.append(right[right_list_index])
            right_list_index += 1

        elif right_list_index == right_len:
            sorted_list.append(left[left_ind])
            left_ind += 1

    return sorted_list


def sort_merge_helper(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = sort_merge_helper(array[:mid])
    right = sort_merge_helper(array[mid:])

    return merge(left, right)


print(f'Отсортированный список по возрастанию: {sort_merge_helper(mas.copy())}')
