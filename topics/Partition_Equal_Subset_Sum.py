def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False   # odd sum can't split into two equal halves

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True   # sum of 0 is always achievable (empty subset)

    for num in nums:
        for w in range(target, num - 1, -1):
            dp[w] = dp[w] or dp[w - num]

    return dp[target]


print(can_partition([1, 5, 11, 5]))   # True -> [1,5,5] and [11] both sum to 11
print(can_partition([1, 2, 3, 5]))    # False
