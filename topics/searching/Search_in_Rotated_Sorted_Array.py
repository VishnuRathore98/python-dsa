def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:           # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1               # target is in the sorted left half
            else:
                left = mid + 1
        else:                                  # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1                # target is in the sorted right half
            else:
                right = mid - 1

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(nums, 0))   # 4
print(search_rotated(nums, 3))   # -1
