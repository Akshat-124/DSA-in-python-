class Solution:
    
    def dfs(self, node, adj, visited, stack):
        visited[node] = True
        
        for nei in adj[node]:
            if not visited[nei]:
                self.dfs(nei, adj, visited, stack)
        
        stack.append(node)   # DFS ke baad push karenge
    
    def topoSort(self, V, adj):
        visited = [False] * V
        stack = []
        
        for i in range(V):
            if not visited[i]:
                self.dfs(i, adj, visited, stack)
        
        return stack[::-1]   # reverse karke answer