class Graph:
    def __init__(self):
        self.graph = {}
        self.weighted_graph = {}

    # ------------------ UNWEIGHTED ------------------
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    # ------------------ WEIGHTED ------------------
    def add_weighted_edge(self, u, v, w):
        if u not in self.weighted_graph:
            self.weighted_graph[u] = []
        if v not in self.weighted_graph:
            self.weighted_graph[v] = []

        self.weighted_graph[u].append((v, w))
        self.weighted_graph[v].append((u, w))

    # ------------------ DISPLAY ------------------
    def display(self):
        print("Unweighted Graph:")
        for node in self.graph:
            print(node, "->", self.graph[node])

        print("\nWeighted Graph:")
        for node in self.weighted_graph:
            print(node, "->", self.weighted_graph[node])

    # ------------------ DFS ------------------
    def dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        for nei in self.graph[node]:
            if nei not in visited:
                self.dfs(nei, visited)

    # ------------------ BFS ------------------
    def bfs(self, start):
        from collections import deque

        visited = set()
        q = deque([start])
        visited.add(start)

        while q:
            node = q.popleft()
            print(node, end=" ")

            for nei in self.graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

    # ------------------ CYCLE DETECTION ------------------
    def has_cycle(self, node, parent, visited):
        visited.add(node)

        for nei in self.graph[node]:
            if nei not in visited:
                if self.has_cycle(nei, node, visited):
                    return True
            elif nei != parent:
                return True
        return False


# ================== EXAMPLE ==================

g = Graph()

# Unweighted edges
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)  # cycle banega

# Weighted edges
g.add_weighted_edge(1, 2, 5)
g.add_weighted_edge(1, 3, 10)
g.add_weighted_edge(2, 4, 3)

# Display
g.display()

# DFS
print("\nDFS Traversal:")
visited = set()
g.dfs(1, visited)

# BFS
print("\nBFS Traversal:")
g.bfs(1)

# Cycle Detection
print("\nCycle Present:", g.has_cycle(1, -1, set()))