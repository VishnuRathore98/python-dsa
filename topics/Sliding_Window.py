def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])   # sum of first window
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]   # add new element, remove leftmost
        max_sum = max(max_sum, window_sum)

    return max_sum


nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(nums, k))   # 9 -> [5,1,3]
