def max_activities(activities):
    # activities: list of (start, end) tuples
    activities.sort(key=lambda x: x[1])   # sort by end time
    count = 1
    last_end = activities[0][1]

    for start, end in activities[1:]:
        if start >= last_end:
            count += 1
            last_end = end

    return count


activities = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
print(max_activities(activities))   # 4
