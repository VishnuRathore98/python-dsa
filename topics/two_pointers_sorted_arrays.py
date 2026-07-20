def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

arr = [1, 3, 4, 6, 8, 10]
print(two_sum_sorted(arr, 10))   # [1, 4] → 3 + ... wait, check: 3+? 
