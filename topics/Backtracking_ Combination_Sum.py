def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return   # prune this branch, overshot the target

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])   # i, not i+1 -> allows reuse
            path.pop()

    backtrack(0, [], target)
    return result


print(combination_sum([2, 3, 6, 7], 7))
# [[2,2,3], [7]]
