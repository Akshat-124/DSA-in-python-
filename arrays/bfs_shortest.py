from collections import deque

class Solution:
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])

        q = deque()
        dist = [[-1] * m for _ in range(n)]

        # Step 1: Sabhi 0 ko queue me daalo
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                    dist[i][j] = 0

        # 4 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: BFS chalao
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist