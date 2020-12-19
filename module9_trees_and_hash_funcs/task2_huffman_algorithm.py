"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

from module9_trees_and_hash_funcs.my_node import MyNode
from collections import deque


def binary_search(bin_search_tree, char, path=''):
    if bin_search_tree.val == char:
        return f'Код символа \'{char}\' {path}'

    if char < bin_search_tree.val and bin_search_tree.left != None:
        return binary_search(bin_search_tree.left, char, path=f'{path}0')

    if char > bin_search_tree.val and bin_search_tree.right != None:
        return binary_search(bin_search_tree.right, char, path=f'{path}1')

    return f'Символ {char} отсутствует в дереве'


s = input('Введите строку для кодировки: ')
# s = 'beep boop beer!'

char_tact = {i: s.count(i) for i in s}
# Результат сортировки может немного отличаться от приведенного в уроке
nodes = deque([MyNode(i, char_tact[i]) for i in sorted(char_tact, key=lambda x: char_tact[x])])

print('Полученные узлы: ', nodes.__repr__())
print('\nПолученная таблица "символ / частота"')
print('_'*25)
print('|\tchar\t|\tcount\t|')
print('_'*25)
for node in nodes:
    print(f"|\t'{node.display_value}'\t\t|\t'{node.value}'\t\t|")
print('_'*25)


while len(nodes) > 1:
    fst_node = nodes.popleft()
    scd_node = nodes.popleft()

    new_node_value = fst_node.value + scd_node.value
    new_node = MyNode(new_node_value, new_node_value, fst_node, scd_node)

    for i in range(len(nodes)):
        if new_node.value <= nodes[i].value:
            nodes.insert(i, new_node)
            break
    else:  # если получаемое значение превысит максимального в очереди, тогда добавим его в конец
        nodes.append(new_node)

print('\nПолученное дерево:\n', new_node)
codes = {}
new_node.walk(codes, "")

print('\nПолученная таблица Хаффмана: ')
print('_'*25)
print('|\tchar\t|\tcode\t|')
print('_'*25)
for char, code in codes.items():
    print(f"|\t'{char}'\t\t|\t'{code}'\t|")
print('_'*25)

encode_str = ''
print('\nВходная строка в бинарном виде: ', ' '.join(format(ord(x), 'b') for x in s))
for i in s:
    encode_str += codes[i] + ' '
print('Выходная (зашифрованная) строка: %s' % (encode_str))
