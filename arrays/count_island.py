class Solution:
    def countDistinctIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        visited = [[False] * m for _ in range(n)]
        shapes = set()
        
        def dfs(r, c, base_r, base_c, shape):
            visited[r][c] = True
            
            # relative position store karenge
            shape.append((r - base_r, c - base_c))
            
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 1:
                    dfs(nr, nc, base_r, base_c, shape)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    shape = []
                    dfs(i, j, i, j, shape)
                    shapes.add(tuple(shape))
        
        return len(shapes)