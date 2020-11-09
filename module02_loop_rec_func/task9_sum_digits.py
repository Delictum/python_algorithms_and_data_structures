"""
The task 9:
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

max_number = 0
max_sum = 0
n = input('Введите натуральное число: ')

while n != '':
    s = 0
    for dig in n:
        s += int(dig)
    if max_sum < s:
        max_sum = s
        max_number = n
    n = input('Введите натуральное число: ')
print(max_number)
