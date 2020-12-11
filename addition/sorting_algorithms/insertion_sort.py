import random


size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(f'Исходный список: {array}')


def sort_by_insert(mas):
    n = 0
    for i in range(1, len(mas)):
        spam = mas[i]
        j = i
        while mas[j - 1] > spam and j > 0:
            n += 1
            mas[j] = mas[j-1]
            j -= 1
        mas[j] = spam
    print(f'Количество проходов while: {n}')
    return mas


print(f'Отсортированный список: {sort_by_insert(array.copy())}')
