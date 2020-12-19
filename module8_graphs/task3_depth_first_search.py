"""
Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
from random import randint


def generate_adjacency_list_graph(n: "int count vertex"):
    graph = []
    for i in range(n):
        vertex_path = []
        for j in range(n):
            if i != j and randint(0, 1):  # если не создание петли и 50% вероятность создания
                vertex_path.append(j)
            elif j == n - 1:  # если ни разу не везло и вершина не связалась с другими, принудительно свяжем с последней
                vertex_path.append(j)
        graph.append(vertex_path)
    return graph


def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # print(start)
    for next in set(graph[start]) - visited:
        depth_first_search(graph, next, visited)
    return visited


n = int(input('Введите кол-во вершин для генерации графа: '))
g = generate_adjacency_list_graph(n)
print(*g, sep='\n')

print(depth_first_search(g, 0))
