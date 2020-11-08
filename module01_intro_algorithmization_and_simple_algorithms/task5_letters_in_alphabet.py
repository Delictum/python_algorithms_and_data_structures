"""
The task 5:
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

Решения корректны для латинского алфавита.
Для работы с люыбм другим измените значение переменной first_letter_in_alphabet на первую букву требуемого алфавита
"""

first_letter_in_alphabet = 'a'

num_letter_in_alphabet = int(input('Номер буквы в алфавите: '))
founded_letter = ord(first_letter_in_alphabet) + num_letter_in_alphabet - 1
print('Это буква', chr(founded_letter))
