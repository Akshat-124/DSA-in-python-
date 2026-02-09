def is_safe(maze, x, y, n, visited):                                     #optimal TC=O(4^(n^2)),SC=O(n^2)
    return (0 <= x < n and 0 <= y < n and 
            maze[x][y] == 1 and not visited[x][y])
def solve_maze_util(maze, x, y, n, visited, path, result):
    if x == n - 1 and y == n - 1:
        result.append(path)
        return
    visited[x][y] = True
    if is_safe(maze, x + 1, y, n, visited):
        solve_maze_util(maze, x + 1, y, n, visited, path + "D", result)
    if is_safe(maze, x, y - 1, n, visited):
        solve_maze_util(maze, x, y - 1, n, visited, path + "L", result)
    if is_safe(maze, x, y + 1, n, visited):
        solve_maze_util(maze, x, y + 1, n, visited, path + "R", result)
    if is_safe(maze, x - 1, y, n, visited):
        solve_maze_util(maze, x - 1, y, n, visited, path + "U", result)
    visited[x][y] = False
def solve_maze(maze):
    n = len(maze)
    result = []
    if maze[0][0] == 0:
        return result
    visited = [[False for _ in range(n)] for _ in range(n)]
    solve_maze_util(maze, 0, 0, n, visited, "", result)
    return result
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

print(solve_maze(maze))
