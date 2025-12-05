
def main():
 # nums = [5,2,6,3,8,12,10,9] # Jumbled random numbers
  nums = [3,2,6,4,1,9,5,7,8]; # jumbled 1-9 numbers
  sort(nums);
  print(nums);


# Rename as per algorithm name
def sort (nums):
  return -1


# Swap values
def swap(nums,  index, correctIndex):
  temp = nums[index];
  nums[index] = nums[correctIndex]
  nums[correctIndex] = temp

if __name__ == "__main__":
    main()