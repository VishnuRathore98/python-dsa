def top_k_frequent_bucket(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]   # index = frequency
    for num, freq in count.items():
        buckets[freq].append(num)
    
    result = []
    for freq in range(len(buckets) - 1, 0, -1):   # highest freq first
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result

print(top_k_frequent_bucket(nums, k))   # [1, 2]
