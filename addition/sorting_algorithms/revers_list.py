import random


size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(f'Исходный список: {array}')


def reverse(mas):
    for i in range(len(mas) // 2):
        mas[i], mas[len(mas) - i - 1] = mas[len(mas) - i - 1], mas[i]
    return mas


print(f'Перевернутый список: {reverse(array.copy())}')
array.reverse()
print(f'Перевернутый список: {array}')
