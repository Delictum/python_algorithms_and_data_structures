"""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

n = int(input())
graph = []
counter = 0

for i in range(n):
    lst = []

    for j in range(n):
        if i == j:
            lst.append(0)
        else:
            lst.append(1)
            counter += 1

    graph.append(lst)

print(*graph, sep='\n')
print(f'Количество рукопожатий: {counter // 2}')
