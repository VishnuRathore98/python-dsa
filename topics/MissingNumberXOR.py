def missing_number_xor(nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result

print(missing_number_xor([3, 0, 1]))   # 2
