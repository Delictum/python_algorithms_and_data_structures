"""
The task 8:
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

fst_num = float(input('Введите первое число: '))
scd_num = float(input('Введите второе число: '))
tht_num = float(input('Введите третье число: '))

if fst_num > scd_num > tht_num or fst_num < scd_num < tht_num:
    print(f'Средним является {scd_num}')
elif scd_num > fst_num > tht_num or scd_num < fst_num < tht_num:
    print(f'Средним является {fst_num}')
else:
    print(f'Средним является {tht_num}')
