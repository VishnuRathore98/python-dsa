def rob_circular(nums):
    if len(nums) == 1:
        return nums[0]

    def rob_linear(houses):
        prev2, prev1 = 0, 0
        for num in houses:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1

    # can't rob both first and last house, so try both scenarios and take the best
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

print(rob_circular([2, 3, 2]))   # 3 -> can't take both house 0 and house 2
