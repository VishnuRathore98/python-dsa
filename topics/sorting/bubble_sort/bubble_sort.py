
def main():
  nums = [5,2,6,3,8,12,10,9] # Jumbled random numbers
#   nums = [3,2,6,4,1,9,5,7,8]; # jumbled 1-9 numbers
  sortedNums = bubbleSort(nums);
  print(sortedNums);


# Rename as per algorithm name
def bubbleSort (nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
    return nums


# Swap values
def swap(nums,  index, correctIndex):
  temp = nums[index];
  nums[index] = nums[correctIndex]
  nums[correctIndex] = temp

if __name__ == "__main__":
    main()