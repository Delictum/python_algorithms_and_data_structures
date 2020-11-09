"""
The task 6:
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
"""
import random


guesses_num = random.randint(1, 100)
for i in range(10):
    num = int(input('Введите число: '))
    if num == guesses_num:
        print('Успех')
        break
    elif num < guesses_num:
        print('Ваше число меньше')
    else:
        print('Ваше число больше')
else:
    print(f'Было загадано число {guesses_num}')