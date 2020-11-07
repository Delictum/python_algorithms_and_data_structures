# put your python code here

import sys
sys.stdin = open("input.txt", "r")


n = int(input())

list_classes = []
for i in range(n):
    list_classes.append(input())
q = int(input())
list_checked_classes = []
for i in range(q):
    list_checked_classes.append(input())
'''


list_classes = [  # список введённых строк
    'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    'A',
    'B : A',
    'C : A',
    'D : B C',
    'E : D',
    'F : D',
    # а теперь другая ветка наследования
    'X',
    'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    'Z : X',
    'V : Z Y',
    'W : V',
]

list_checked_classes = [  # список введённых запросов
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'X QWE',    # No    # нет такого класса QWE
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
]



list_classes = [
    'classA : classB classC classD classG classH',
    'classB : classC classE classG classH classK classL',
    'classC : classE classD classH classK classL',
    'classE : classD classF classK classL',
    'classD : classG classH',
    'classF : classK',
    'classG : classF',
    'classH : classL',
    'classK : classH classL',
    'classL',
    ]
list_checked_classes = [
    'classK classD',
    'classD classA',
    'classG classD',
    'classH classA',
    'classE classE',
    'classH classG',
    'classE classL',
    'classB classD',
    'classD classL',
    'classD classG',
    'classD classE',
    'classA classF',
    'classA classC',
    'classK classA',
    'classA classH',
    'classK classD',
    'classH classB',
    'classK classB',
    'classD classL',
    'classG classG',
    'classA classH',
    'classK classL',
    'classG classE',
    'classB classA',
    'classC classK',
    'classK classL',
    'classC classL',
    'classG classC',
    'classD classD',
    'classC classG',
    'classE classA',
    'classF classK',
    'classB classG',
    'classH classL',
    'classL classF',
    'classH classG',
    'classD classA',
    'classH classL',
    ]
'''
list_answers = '''Yes
Yes
Yes
Yes
Yes
Yes
No
No
No
No
Yes
No
No
Yes
No
Yes
Yes
Yes
No
Yes
No
No
Yes
Yes
No
No
No
Yes
Yes
No
Yes
No
No
No
Yes
Yes
Yes
No'''.split('\n')


dict_classes = {}
for i in list_classes:    
    if not ' : ' in i:
        dict_classes[i] = set()
        list_classes.remove(i)
        
for i in list_classes: 
    child, parrent = i.split(' : ')

    if not child in dict_classes:
        dict_classes[child] = set()
    if ' ' in parrent:
        parrent = parrent.split()

    if list == type(parrent):
        for j in parrent:
            if j in dict_classes:
                dict_classes[j].add(child)
            else:
                dict_classes[j] = set()
                dict_classes[j].add(child)
        continue

    dict_classes[parrent].add(child)
        

print('START DICT -', dict_classes)

for num in range(2):
    for k, v in dict_classes.items():
        for i in v:
            dict_classes[k] = dict_classes[k].union(dict_classes[i])
 
print('FINISH DICT -', dict_classes)

'''
for i in list_checked_classes:
    parrent, child = i.split()

    if parrent in dict_classes and \
       (child in dict_classes[parrent] or parrent == child):
        print('Yes')
        continue
    print('No')
'''
for i in range(len(list_checked_classes)):
    parrent, child = list_checked_classes[i].split()

    if parrent == child or child in dict_classes[parrent]:
        print('Yes', list_answers[i])
        continue
    print('No', list_answers[i])

