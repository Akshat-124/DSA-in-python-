from itertools import permutations          
def solve_n_queens(n):                            ####bruteforce TC=o(n^m)
    result = []
    for cols in permutations(range(n)):
        if len(set(cols[i] - i for i in range(n))) == n and \
           len(set(cols[i] + i for i in range(n))) == n:
            board = []
            for i in range(n):
                row = ["." for _ in range(n)]
                row[cols[i]] = "Q"
                board.append("".join(row))
            result.append(board)
    return result
print(solve_n_queens(4))

print("------------------------------")

def solve_n_queens_backtracking(n):                 ####optimal TC=o(n!)
    board = [["." for _ in range(n)] for _ in range(n)]
    result = []
    cols = set()
    diag1 = set()   
    diag2 = set()   
    def backtrack(r):
        if r == n:
            result.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            board[r][c] = "Q"
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            backtrack(r + 1)
            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
    backtrack(0)
    return result
print(solve_n_queens_backtracking(4))

