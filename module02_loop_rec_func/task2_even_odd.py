"""
The task 2:
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = input('Введите целое число: ')
count_odd = 0
count_even = 0

for i in num:
    if int(i) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f'Четных: {count_even}, нечетных: {count_odd}')
