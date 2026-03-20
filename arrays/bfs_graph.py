from collections import deque

def bfs(V, adj):
    visited = [False] * V
    result = []
    
    q = deque()
    
    # assuming traversal starts from node 0
    q.append(0)
    visited[0] = True
    
    while q:
        node = q.popleft()
        result.append(node)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    
    return result


# Example usage
V = 5
adj = [
    [1, 2],     # neighbors of 0
    [0, 3, 4],  # neighbors of 1
    [0],        # neighbors of 2
    [1],        # neighbors of 3
    [1]         # neighbors of 4
]

print(bfs(V, adj))