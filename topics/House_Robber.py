def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        # either skip house i (take dp[i-1]) or rob it (dp[i-2] + nums[i])
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


nums = [2, 7, 9, 3, 1]
print(rob(nums))   # 12 -> rob houses 0, 2, 4 (2+9+1=12)
