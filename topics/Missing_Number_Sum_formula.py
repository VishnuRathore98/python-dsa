def missing_number(nums):
    n = len(nums)
    expected = n * (n + 1) // 2   # sum of 0..n
    return expected - sum(nums)

print(missing_number([3, 0, 1]))                    # 2
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
