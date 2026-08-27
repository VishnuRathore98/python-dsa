def backtrack(path, choices):
    if is_solution(path):
        record(path)
        return

    for choice in choices:
        if is_valid(choice, path):
            path.append(choice)          # make the choice
            backtrack(path, choices)     # explore further
            path.pop()                   # undo the choice (backtrack!)

