class Solution:
    def isCycle(self, V, adj):
        visited = [False] * V

        def dfs(node, parent):
            visited[node] = True

            for nei in adj[node]:
                if not visited[nei]:
                    if dfs(nei, node):
                        return True
                elif nei != parent:
                    return True

            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True

        return False