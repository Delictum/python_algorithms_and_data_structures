from collections import namedtuple


graph = []

graph.append([1, 2])
graph.append([0, 2, 3])
graph.append([0, 1])
graph.append([1])

print(*graph, sep='\n')
print('*'*50)

graph2 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1}
}

print(graph2)
print('*'*50)

Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph3 = []

graph3.append([Vertex(1, 2), Vertex(2, 3)])
graph3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph3.append([Vertex(0, 3), Vertex(1, 2)])
graph3.append([Vertex(1, 1)])

print(*graph3, sep='\n')

for v in graph3[1]:
    if v.vertex == 3:
        print(True)


class Graph:
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge


graph4 = [(0, 1), (0, 2), (1, 2), (2, 1), (1, 3), ]
print(*graph4, sep='\n')
