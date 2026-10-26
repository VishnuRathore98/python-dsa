from collections import Counter

def least_interval(tasks, n):
    counts = Counter(tasks)
    max_count = max(counts.values())              # frequency of the most common task
    max_count_tasks = sum(1 for c in counts.values() if c == max_count)  # how many tasks tie for most frequent

    # formula: (max_count - 1) full cycles of length (n+1), plus the final batch of tied-max tasks
    intervals = (max_count - 1) * (n + 1) + max_count_tasks

    return max(intervals, len(tasks))   # can't be less than total task count (no idle needed)


tasks = ["A","A","A","B","B","B"]
n = 2
print(least_interval(tasks, n))   # 8 -> A B idle A B idle A B
