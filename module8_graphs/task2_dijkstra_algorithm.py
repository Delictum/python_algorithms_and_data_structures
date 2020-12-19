"""
Реализовать алгоритм Дейкстры, и чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""

from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    init_start = start  # запоминает от какого элемента начинается обход
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    shortest_path = {i: deque() for i in range(length)}  # Хранит кратчайшие пути
    shortest_path[start] = deque([start])  # Путь к искомой вершине сразу же равен 0

    while min_cost < float('inf'):

        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                current_cost = vertex + cost[start]
                if cost[i] > current_cost:
                    cost[i] = current_cost
                    parent[i] = start

                    shortest_path[i].append(start)

                    # Этот блок выполняется в том случае, если был найден более короткий путь.
                    # Тогда он добавляет вершины из этого более "легкого" пути
                    if shortest_path[start][0] != init_start:
                        for j in range(len(shortest_path[start])-1, -1, -1):
                            if shortest_path[j] not in shortest_path[i]:
                                shortest_path[i].appendleft(shortest_path[start][j])

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
            # shortest_path[i].append(start)

    for k, v in shortest_path.items():
        if len(v) > 0 and k != init_start:
            if v[0] != init_start:  # Если в пути не была добавлена в начало стартовая вершина, то поместим её в начало
                v.appendleft(init_start)
            v.append(k)  # Добавим к пути поиска вершины саму эту вершину в конец пути
        elif len(v) == 0:
            v.append('Нет пути')

    return cost, shortest_path


s = int(input('От какой вершины идти: '))
# print(dijkstra(g, s))
cost, shortest_path = dijkstra(g, s)
print(f'Наименьшие стоимости к вершинам: {cost}')

print(f'Лучшие маршруты: ')
for k, v in shortest_path.items():
    print(k, end=' -> ')
    for i in v:
        print(i, end=' | ')
    print()
