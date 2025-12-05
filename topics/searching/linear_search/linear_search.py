
def main():
  #  nums = [1,2,3,4,5,6,7,8,9] # ascending ordered 
  nums = [5,2,6,3,8,12,10,9]
  searchVal = 10;
  foundAtIndex = linearSearch(nums, searchVal);

  print(foundAtIndex);


def linearSearch(nums, val):
  for i in range(len(nums)):
    if (nums[i] == val):
      return i;
  return -1;

if __name__ == "__main__":
    main()