from collections import deque

class Solution:
    def isCycle(self, V, adj):
        visited = [False] * V

        for i in range(V):
            if not visited[i]:
                if self.bfs(i, adj, visited):
                    return True
        return False

    def bfs(self, start, adj, visited):
        q = deque()
        q.append((start, -1))
        visited[start] = True

        while q:
            node, parent = q.popleft()

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, node))
                elif neighbor != parent:
                    return True

        return False
V = 5
adj = [
    [1],
    [0, 2, 4],
    [1, 3],
    [2, 4],
    [1, 3]
]

obj = Solution()
print(obj.isCycle(V, adj))