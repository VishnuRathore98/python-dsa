def single_number(nums):
    result = 0
    for num in nums:
        result ^= num   # pairs cancel out
    return result

print(single_number([4, 1, 2, 1, 2]))   # 4
