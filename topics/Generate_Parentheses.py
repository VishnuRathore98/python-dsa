def generate_parentheses(n):
    result = []

    def backtrack(path, open_count, close_count):
        if len(path) == 2 * n:
            result.append("".join(path))
            return

        if open_count < n:
            path.append("(")
            backtrack(path, open_count + 1, close_count)
            path.pop()   # undo

        if close_count < open_count:
            path.append(")")
            backtrack(path, open_count, close_count + 1)
            path.pop()   # undo

    backtrack([], 0, 0)
    return result


print(generate_parentheses(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
