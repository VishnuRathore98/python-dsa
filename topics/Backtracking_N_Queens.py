def solve_n_queens(n):
    result = []
    board = [['.'] * n for _ in range(n)]

    def is_safe(row, col):
        for r in range(row):
            if board[r][col] == 'Q':
                return False
        for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[r][c] == 'Q':
                return False
        for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[r][c] == 'Q':
                return False
        return True

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'   # undo

        return

    backtrack(0)
    return result


solutions = solve_n_queens(4)
for sol in solutions:
    for row in sol:
        print(row)
    print()
