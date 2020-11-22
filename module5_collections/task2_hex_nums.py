"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

'''
Программный код получился объемный, т.к. оптимизирован под решение любого переданного количества чисел
'''

import argparse
import copy
from collections import deque


hexadecimal_values = '0123456789ABCDEF'
relationships = {hexadecimal_values[i]: i for i in range(len(hexadecimal_values))}
relationships_reverse = {v: k for k, v in relationships.items()}


def get_sum_hex_nums(*args):
    max_len = len(max(args, key=len))
    sum_result = deque()
    spam = 0

    for i in range(max_len):
        digits = []
        for j in args:
            digits.append(j.pop()) if j else digits.append('0')

        sum_nums = 0
        for j in digits:
            sum_nums += relationships[j]
        sum_nums += spam

        if sum_nums < 16:
            spam = 0
        else:
            spam = sum_nums // 16
            sum_nums %= 16

        sum_result.appendleft(relationships_reverse[sum_nums])

    if spam:
        sum_result.appendleft(relationships_reverse[spam])
    return sum_result


def get_multiplication_hex_nums(deque_list):
    total_sum_result = deque()

    first = None
    while deque_list:
        if first:
            second = deque_list[0]
        else:
            first, second = deque_list[0], deque_list[1]
            del deque_list[1]
        del deque_list[0]

        i = 0
        for _ in second.copy():
            s = second.pop() if second else '0'

            first_div = first.copy()

            sum_result = deque()
            spam = 0
            for _ in first:
                f = first_div.pop() if first else '0'

                div_nums = relationships[s] * relationships[f] + spam
                if div_nums < 16:
                    spam = 0
                else:
                    spam = div_nums // 16
                    div_nums %= 16

                sum_result.appendleft(relationships_reverse[div_nums])

            if spam:
                sum_result.appendleft(relationships_reverse[spam])
            for _ in range(i):
                sum_result.append('0')
            i += 1
            total_sum_result.appendleft(sum_result)
        first = get_sum_hex_nums(*total_sum_result)
    return first


parser = argparse.ArgumentParser()

parser.add_argument('-f', '--first')
parser.add_argument('-s', '--second')

args = parser.parse_args()
first_arg, second_arg = args.first, args.second

first_init = deque(first_arg if first_arg else input('Введите первое шестнадцатеричное число: '))
second_init = deque(second_arg if second_arg else input('Введите второе шестнадцатеричное число: '))

print(f'Полученная сумма: {get_sum_hex_nums(first_init.copy(), second_init.copy())}')
print(f'Полученное произведение: {get_multiplication_hex_nums([first_init.copy(), second_init.copy()])}')

'''
n = int(input('Введите количество используемых чисел: '))
numbers = []
for i in range(n):
    numbers.append(deque(input('Введите первое шестнадцатеричное число: ')))

print(f'Полученная сумма: {get_sum_hex_nums(*copy.deepcopy(numbers))}')
print(f'Полученное произведение: {get_multiplication_hex_nums(copy.deepcopy(numbers))}')

EXAMPLE USAGE:
Введите количество используемых чисел: 4
Введите первое шестнадцатеричное число: BA3C40F
Введите первое шестнадцатеричное число: 23
Введите первое шестнадцатеричное число: F0F0F0
Введите первое шестнадцатеричное число: 123

Полученная сумма: deque(['C', '9', '4', 'B', '6', '4', '5'])
Полученное произведение: deque(['1', 'B', '3', 'D', '8', 'E', '3', '3', '6', '4', 'B', 'C', 'F', 'C', 'A', '9', '0'])
'''
