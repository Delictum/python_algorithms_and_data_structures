import random


size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(f'Исходный список: {array}')


def sort_by_selection(mas):
    for i in range(len(mas)):
        idx_min = i
        for j in range(i + 1, len(mas)):
            if mas[j] < mas[idx_min]:
                idx_min = j
        mas[idx_min], mas[i] = mas[i], mas[idx_min]
    return mas


print(f'Отсортированный список: {sort_by_selection(array.copy())}')
