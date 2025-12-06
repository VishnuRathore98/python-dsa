# Bubble Sort

- A simple comparison-based sorting algorithm that repeatedly steps through the list
- Works by comparing adjacent elements and swapping them if they are in the wrong order
- The algorithm gets its name because smaller elements "bubble" to the top of the list with each pass
- After each complete pass through the list, the largest unsorted element is placed in its correct position at the end


# Limitations
- **Inefficient for large datasets** - Has quadratic time complexity making it slow for large lists
- Not suitable for real-world applications with large data
- Simple to understand but not practical for production use
- Many better alternatives exist (Quick Sort, Merge Sort, etc.)


# ⏰ Time Complexity
Let n be the number of elements in the array or list.

Best Case: O(n) - When the array is already sorted, we can optimize to stop early if no swaps occur.
Average Case: O(n²) - Requires multiple passes through the array, comparing and swapping elements.
Worst Case: O(n²) - When the array is sorted in reverse order, maximum comparisons and swaps are needed.

➡️ This is because bubble sort uses nested loops, with the outer loop running n times and the inner loop running up to n times, resulting in quadratic performance.


# 🌌 Space Complexity
O(1) – Bubble sort is an in-place sorting algorithm that only uses a constant amount of extra space for temporary variables (like the swap operation). No additional data structures are required.