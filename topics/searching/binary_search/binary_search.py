
def main():
  nums = [1,2,3,4,5,6,7,8,9,10]; # ascending ordered 
  # nums = [5,2,6,3,8,12,10,9];
  searchVal = 3;
  foundAtIndex = binarySearch(nums, searchVal);
  print(foundAtIndex);


# Rename as per algorithm name
def binarySearch( nums,  val):
  s = 0;
  e = len(nums) - 1;

  while (s<=e):
    mid = (s+e) // 2;
    if (nums[mid] == val):
      return mid;
    elif (nums[mid] > val):
      e = mid-1;
    else:
      s = mid +1;

  return -1;

if __name__ == "__main__":
    main()