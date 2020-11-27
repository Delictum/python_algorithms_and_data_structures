"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.

Примечания/ответы по пунктам условия к решениям задачи в конце файла
"""

import sys
from random import randint

# В функциях производятся повторные замеры с большинством уже замеренных значений.
# Это сделано на случаи больших чисел, т.к. они создадут новые ссылки в памяти несмотря на равенство значений


array = [randint(-999, 999) for i in range(10)]
common_memory_links = {}  # ключ - ссылка в памяти, значение - объект, хранящийся по ссылке


def get_total_size(x, memory_links, size=0):
    link = id(x)
    if link in memory_links:  # если ссылка уже была добавлена, значит объем потребления памяти не изменится
        return size

    memory_links[link] = x

    if not size:
        size = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, '__items__'):
            for i in x.items():
                size = get_total_size(i, memory_links, size + sys.getsizeof(i))

        elif not isinstance(x, str):
            for i in x:
                size = get_total_size(i, memory_links, size + sys.getsizeof(i))

    # print(sys.getsizeof(x))
    return size


def implementation1(mas, memory_links1):
    size = 0

    # реальные затраты памяти нахождения индексов могу быть выше, т.к. это функции built-in -
    # т.е. достоверно вычислить занятую память внутри метода index навряд ли возможно

    mi = min(mas)
    ma = max(mas)

    size += get_total_size(mi, memory_links1)
    size += get_total_size(ma, memory_links1)

    min_i = mas.index(mi)
    max_i = mas.index(ma)

    size += get_total_size(min_i, memory_links1)
    size += get_total_size(max_i, memory_links1)

    print(f'Позиция минимального: {min_i}. Максимального: {max_i}')
    if min_i > max_i:
        min_i, max_i = max_i, min_i
        size += get_total_size(min_i, memory_links1)
        size += get_total_size(max_i, memory_links1)

    s = 0
    size += get_total_size(s, memory_links1)

    min_i1 = min_i + 1
    size += get_total_size(min_i1, memory_links1)

    for i in range(min_i1, max_i):
        size += get_total_size(i, memory_links1)

        s += mas[i]
        size += get_total_size(s, memory_links1)
    print('Полученная сумма: ', s)

    print('Общий размер затраченной памяти в реализации:', size, '\n')


def implementation2(mas, memory_links2):
    size = 0

    # нет смысла проверять min(mas) & max(mas), т.к. они уже включены в подсчет памяти при измерении списка
    mi = min(mas)
    ma = max(mas)

    size += get_total_size(mi, memory_links2)
    size += get_total_size(ma, memory_links2)

    min_i = mas.index(mi)
    max_i = mas.index(ma)

    size += get_total_size(min_i, memory_links2)
    size += get_total_size(max_i, memory_links2)

    print(f'Позиция минимального: {min_i}. Максимального: {max_i}')
    if min_i > max_i:
        min_i, max_i = max_i, min_i
        size += get_total_size(min_i, memory_links2)
        size += get_total_size(max_i, memory_links2)

    min_i1 = min_i + 1
    size += get_total_size(min_i1, memory_links2)

    # реальные затраты памяти могу быть выше, т.к. это функция built-in -
    # т.е. достоверно вычислить занятую память внутри sum навряд ли возможно
    s = sum(mas[min_i1:max_i])
    size += get_total_size(s, memory_links2)

    print('Полученная сумма: ', s)

    print('Общий размер затраченной памяти в реализации:', size, '\n')


def implementation3(mas, memory_links3):
    """
    Решение преподавателя
    """

    size = 0

    idx_min = 0
    idx_max = 0

    size += get_total_size(idx_min, memory_links3)  # одновременно отработает для idx_max

    for i in range(1, len(mas)):
        size += get_total_size(i, memory_links3)
        if array[i] < array[idx_min]:
            idx_min = i
            size += get_total_size(idx_min, memory_links3)
        elif array[i] > array[idx_max]:
            idx_max = i
            size += get_total_size(idx_max, memory_links3)

    print(f'Позиция минимального: {idx_min}. Максимального: {idx_max}')

    if idx_min > idx_max:
        idx_min, idx_max = idx_max, idx_min
        size += get_total_size(idx_min, memory_links3)
        size += get_total_size(idx_max, memory_links3)

    s = 0  # вычисление памяти уже отработало здесь: idx_min = 0; size += get_total_size(idx_min, memory_links3)

    # i был подсчитан в прошлом цикле
    for i in range(idx_min + 1, idx_max):
        size += get_total_size(i, memory_links3)
        s += mas[i]
        size += get_total_size(s, memory_links3)

    print('Полученная сумма: ', s)

    print('Общий размер затраченной памяти в реализации:', size, '\n')


print('Используемый список:', array)
print('Общий размер списка:', get_total_size(array, common_memory_links), '\n')

# в эти функции передаю копии словарей, чтобы подсчет памяти первой реализации не повлиял на остальные и т.п.
implementation1(array, common_memory_links.copy())
implementation2(array, common_memory_links.copy())
implementation3(array, common_memory_links.copy())


'''
a. Задачи первых трех модулей в принципе слишком простые, чтобы написать разительно отличные примеры.
Рассматриваемая задача из 3 модуля под номером 6:
"В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."

b. Реализации находятся в функциях: implementation1, implementation2, implementation3.

c. Тест №1:
------------------------------------------------------------------------------------------------------------------------
Используемый список: [-852, -426, -24, -605, 1, -705, 864, 890, -732, 204]
Общий размер списка: 240 

Позиция минимального: 0. Максимального: 7
Полученная сумма:  -895
Общий размер затраченной памяти в реализации: 180 

Позиция минимального: 0. Максимального: 7
Полученная сумма:  -895
Общий размер затраченной памяти в реализации: 40 

Позиция минимального: 0. Максимального: 7
Полученная сумма:  -895
Общий размер затраченной памяти в реализации: 208 
------------------------------------------------------------------------------------------------------------------------

Тест №2
------------------------------------------------------------------------------------------------------------------------
Используемый список: [371, -406, 343, -571, 43, -120, 587, 833, 853, -901]
Общий размер списка: 240 

Позиция минимального: 9. Максимального: 8
Полученная сумма:  0
Общий размер затраченной памяти в реализации: 40 

Позиция минимального: 9. Максимального: 8
Полученная сумма:  0
Общий размер затраченной памяти в реализации: 40 

Позиция минимального: 9. Максимального: 8
Полученная сумма:  0
Общий размер затраченной памяти в реализации: 138 
------------------------------------------------------------------------------------------------------------------------

Тест №3
------------------------------------------------------------------------------------------------------------------------
Используемый список: [-411, -999, -985, -684, 163, 820, 726, 485, -197, 955]
Общий размер списка: 240 

Позиция минимального: 1. Максимального: 9
Полученная сумма:  328
Общий размер затраченной памяти в реализации: 236 

Позиция минимального: 1. Максимального: 9
Полученная сумма:  328
Общий размер затраченной памяти в реализации: 56 

Позиция минимального: 1. Максимального: 9
Полученная сумма:  328
Общий размер затраченной памяти в реализации: 236 
------------------------------------------------------------------------------------------------------------------------

sys.version - 3.7.4
sys.platform - (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] win32

d. Наиболее оптимальный implementation2, если предполагать работу функций из built-in более ресурсоемкими. 
По той же самой причине implementation1 должна отработать менее затратно, чем implementation3.
'''
