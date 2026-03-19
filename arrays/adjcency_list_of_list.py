class GraphList:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for i in range(self.n):
            print(i, "->", self.graph[i])


g = GraphList(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(3, 4)

g.display()