def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # 0 = unvisited, 1 = visiting (in current DFS path), 2 = fully done
    state = [0] * num_courses

    def has_cycle(course):
        if state[course] == 1:
            return True          # found a course we're currently processing -> cycle
        if state[course] == 2:
            return False         # already confirmed safe

        state[course] = 1        # mark as "in progress"
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True
        state[course] = 2        # mark as fully safe
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True


# Example: 0 depends on 1, 1 depends on 0 -> cycle -> impossible
print(can_finish(2, [[0, 1], [1, 0]]))   # False

# Example: 0 depends on 1 -> no cycle -> possible
print(can_finish(2, [[0, 1]]))            # True

# Example: more complex, no cycle
print(can_finish(4, [[1,0],[2,0],[3,1],[3,2]]))   # True
