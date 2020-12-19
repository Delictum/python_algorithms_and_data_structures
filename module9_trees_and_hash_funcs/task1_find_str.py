"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* задача считается решённой, если в коде использована функция вычисления хеша (hash(), sha1() или любая другая из модуля hashlib)
"""

# Строить бинарное дерево было необязательно, это для наглядности. И рекурсия с деревом тоже необязательно,
# но так как этот учебный модуль в том числе и про деревья, поэтому захватил обе темы в одном задании

import functools
import hashlib

from module9_trees_and_hash_funcs.my_node import MyNode


hashes = set()


@functools.lru_cache()
def generate_tree(root):
    if len(root.display_value) < 2:
        return root

    left_sub = root.display_value[:-1]
    left_hash = int(hashlib.sha1(left_sub.encode('utf-8')).hexdigest(), base=16)

    root.left = MyNode(left_sub, left_hash)
    hashes.add(left_hash)

    right_sub = root.display_value[1:]
    right_hash = int(hashlib.sha1(right_sub.encode('utf-8')).hexdigest(), base=16)

    root.right = MyNode(right_sub, right_hash)
    hashes.add(right_hash)

    return MyNode(root.display_value, root.value, generate_tree(root.left), generate_tree(root.right))


s = input('Введите строку: ')
# s = 'Hello'

root_hash = int(hashlib.sha1(s.encode('utf-8')).hexdigest(), base=16)
basic_root = MyNode(s, root_hash)

generate_tree(basic_root)

print('Полученное дерево из всех возможных подстрок: ')
print(basic_root)

new_root = MyNode(basic_root.display_value, basic_root.value)


def generate_binary_tree(tree):
    if tree is not None:
        generate_binary_tree(tree.left)
        generate_binary_tree(tree.right)
        new_root.insert(tree.display_value, tree.value)


generate_binary_tree(basic_root)

print('Полученное бинарное дерево (только уникальные подстроки): ')
print(new_root)

print('Количество уникальных подстрок (подсчитано количество элементов в бинарном дереве):', MyNode.count_element)
print(f'\nПолученные хэши в множестве: {hashes}\nКоличество хэшей исходя из длины множества: {len(hashes)}')
