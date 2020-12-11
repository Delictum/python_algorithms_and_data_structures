import random


size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(f'Исходный список: {array}')


def sort_by_shell(mas):
    assert len(mas) < 4000, 'Список слишком большой. Используйте другую сортировку'

    def new_increment(arr):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(arr) <= inc[-1]:
            inc.pop()
        while inc:
            yield inc.pop()

    n = 0
    for increment in new_increment(mas):
        for i in range(increment, len(mas)):
            for j in range(i, increment - 1, -increment):
                n += 1
                if mas[j - increment] <= mas[j]:
                    break
                mas[j], mas[j - increment] = mas[j - increment], mas[j]
    print(f'Количество совершенных проходов внутреннего цикла: {n}')
    return mas


print(f'Отсортированный список: {sort_by_shell(array.copy())}')
