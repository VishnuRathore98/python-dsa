def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])   # every path is a valid subset, record it now
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)   # move forward, can't reuse earlier elements
            path.pop()               # undo

    backtrack(0, [])
    return result


print(subsets([1, 2, 3]))
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
