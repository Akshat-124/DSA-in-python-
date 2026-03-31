from collections import deque

class Solution:
    def numEnclaves(self, grid):
        n = len(grid)
        m = len(grid[0])

        q = deque()

        # Step 1: boundary ke saare 1's queue me daalo
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    if grid[i][j] == 1:
                        q.append((i, j))
                        grid[i][j] = 0   # visited mark

        # 4 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: BFS chalao boundary se connected saare 1's hata do
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    grid[nr][nc] = 0

        # Step 3: jo 1 bache hain wahi enclaves hain
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1

        return count