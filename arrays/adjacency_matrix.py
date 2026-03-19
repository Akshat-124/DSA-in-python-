class GraphMatrix:
    def __init__(self, n):
        self.n = n
        self.graph = [[0]*n for _ in range(n)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def display(self):
        for row in self.graph:
            print(row)


g = GraphMatrix(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(3, 4)

g.display()