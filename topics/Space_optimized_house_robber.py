def rob_optimized(nums):
    if not nums:
        return 0
    prev2, prev1 = 0, 0   # dp[i-2], dp[i-1]

    for num in nums:
        current = max(prev1, prev2 + num)
        prev2, prev1 = prev1, current

    return prev1

print(rob_optimized(nums))   # 12
