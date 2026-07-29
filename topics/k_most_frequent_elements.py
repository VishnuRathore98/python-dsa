import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)   # {value: frequency}
    
    # heap of (frequency, value) — keep only k largest by frequency
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)   # remove lowest frequency
    
    return [num for freq, num in heap]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))   # [2, 1] (order may vary)
