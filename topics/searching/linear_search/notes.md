# Linear Search

- I'd say the easiest search algo, but probably not the most efficient one. 
- We'll traverse to each index linearly and check if the value is found or not.


# Limitations
(Nothing as such of constrainted limitations but--)
- Ineffiecient for large data sets
- No Advantage from sorted data


# ⏰ Time Complexity
Let n be the number of elements in the list.

Best Case: O(1) - The target is found at the first index.
Worst Case: O(n) - The target is not found or is at the last index.
Average Case: O(n) - On average, you'd check about n/2 elements.

# 🌌 Space Complexity
Space Complexity: O(1) — Linear search uses a constant amount of additional memory regardless of the size of the input. No extra data structures are used.