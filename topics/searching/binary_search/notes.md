# Binary Search

- An Effient and very fast way to search for elements in Ordered list
- Works on the basis of divide and conquer method in 
- Basically you'd keep track of start and end values and calculate the mid value to compare, since it's an ordered list you can adjust the start and end value of the basis of mid value.


# Limitations
- Limited to only **Ordered List** List, either ascending or descending.
- Extremely Effiecient for large data sets


# ⏰ Time Complexity
Let n be the number of elements in the sorted array or list.

Best Case: O(1) - Target is found at the middle on the first try.
Average Case: O(log n) - Each comparison halves the search space.
Worst: O(log n) - Target is in the last level of recursion or not present at all.

➡️ This is because binary search divides the input in half with each step, leading to logarithmic performance.

# 🌌 Space Complexity
Iterative Binary Search:
O(1) – No additional space is used beyond a few pointers or variables.

Recursive Binary Search:
O(log n) – Due to recursive function calls stored in the call stack.