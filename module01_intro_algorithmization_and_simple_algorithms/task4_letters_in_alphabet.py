"""
The task 4:
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

Решения корректны для латинского алфавита.
Для работы с люыбм другим измените значение переменной first_letter_in_alphabet на первую букву требуемого алфавита
"""

first_letter_in_alphabet = 'a'

fst_letter = input('Введите первую букву: ')
scd_letter = input('Введите вторую букву: ')

pos_fst_letter = ord(fst_letter) - ord(first_letter_in_alphabet) + 1
pos_scd_letter = ord(scd_letter) - ord(first_letter_in_alphabet) + 1
print('Позиции первой и второй буквы соответственно: %d и %d' % (pos_fst_letter, pos_scd_letter))
print('Количество символов между буквами:', abs(pos_fst_letter - pos_scd_letter) - 1)
