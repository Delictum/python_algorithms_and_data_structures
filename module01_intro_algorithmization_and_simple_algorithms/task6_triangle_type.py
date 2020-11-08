"""
The task 6:
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или равносторонним.
"""

fst_side_len = int(input("Введите певую сторону: "))
scd_side_len = int(input("Введите вторую сторону: "))
tht_side_len = int(input("Введите третью сторону: "))

if fst_side_len + scd_side_len <= tht_side_len or \
        fst_side_len + tht_side_len <= scd_side_len or \
        scd_side_len + tht_side_len <= fst_side_len:
    print("Треугольник не существует")
elif fst_side_len == scd_side_len == tht_side_len:
    print("Равносторонний")
elif fst_side_len != scd_side_len and fst_side_len != tht_side_len and scd_side_len != tht_side_len:
    print("Разносторонний")
else:
    print("Равнобедренный")
