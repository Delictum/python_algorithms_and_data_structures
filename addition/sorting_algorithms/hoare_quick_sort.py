import random


size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(f'Исходный список: {array}')
n = 0


def quick_sort(mas):
    global n

    if len(mas) <= 1:
        return mas

    pivot = random.choice(mas)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in mas:
        n += 1
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        else:
            m_ar.append(item)

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)


print(f'Отсортированный список: {quick_sort(array.copy())}')
print(f'Количество проходов: {n}')
n = 0


def quick_sort_no_memory(mas, fst, lst):
    global n
    if fst >= lst:
        return

    pivot = mas[random.randint(fst, lst)]
    i, j = fst, lst
    while i < j:
        while mas[i] < pivot:
            i += 1
            n += 1
        while mas[j] > pivot:
            j -= 1
            n += 1
        if i <= j:
            mas[i], mas[j] = mas[j], mas[i]
            i, j = i + 1, j - 1
        n += 1

    quick_sort_no_memory(mas, fst, j)
    quick_sort_no_memory(mas, i, lst)


quick_sort_no_memory(array.copy(), 0, len(array) - 1)
print(f'Отсортированный список: {array}')
print(f'Количество проходов: {n}')
