"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""

import argparse
import random
from collections import namedtuple


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count')

args = parser.parse_args()
n = int(args.count) if args.count else int(input('Введите кол-во предприятий: '))

Enterprise = namedtuple('Enterprise', 'name, profit_quarters')

total_avg_profit = 0
enterprises = []

for i in range(n):

    name = input(f'Введите название {i+1} предприятия: ')
    profit_quarters = input(f'Введите прибыль за каждый квартал для {i+1} предприятия через пробел: ').split()
    profit_quarters = [float(j) for j in profit_quarters]

    '''
    name = i
    profit_quarters = [random.uniform(1, 99) for _ in range(4)]
    '''
    enterprise = Enterprise(name, profit_quarters)
    enterprises.append(enterprise)

    enterprise_avg = sum(enterprise.profit_quarters) / 4
    total_avg_profit += enterprise_avg
    print(f'Средняя прибыль предприятия {enterprise.name} составила: {enterprise_avg}')

total_avg_profit /= n

less = []
more = []
print(f'\nСредняя прибыль за год всех предприятий: {total_avg_profit}\n')
for i in range(n):
    enterprise_avg = sum(enterprises[i].profit_quarters) / 4
    more.append(enterprises[i].name) if total_avg_profit < enterprise_avg else less.append(enterprises[i].name)

print(f'Предприятия с меньшим показателем среднего значения: {less}\nС большим показателем среднего значения: {more}')
