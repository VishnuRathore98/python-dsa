import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)   # remove smallest, keep heap size k
    return heap[0]   # smallest in the heap = kth largest overall


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))   # 5
