'''
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления,
которое было зафиксировано максимальное число раз в 2015 году.
'''

import csv
import datetime


primary_types = []
with open('Crimes.csv', 'r') as file:
    lines = csv.reader(file)
    for line in lines:
        try:
            if line[2][6:10] == '2015':
                primary_types.append(line[5])
        except:
            pass

print(max(primary_types, key=primary_types.count))
