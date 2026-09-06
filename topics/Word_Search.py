def word_search(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True   # matched every character

        if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[index]):
            return False

        # mark this cell as visited (temporarily)
        temp = board[r][c]
        board[r][c] = '#'

        found = (backtrack(r + 1, c, index + 1) or
                 backtrack(r - 1, c, index + 1) or
                 backtrack(r, c + 1, index + 1) or
                 backtrack(r, c - 1, index + 1))

        board[r][c] = temp   # undo the mark (backtrack!)

        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True

    return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

print(word_search(board, "ABCCED"))   # True
print(word_search(board, "SEE"))       # True
print(word_search(board, "ABCB"))      # False (would need to reuse the 'C')
