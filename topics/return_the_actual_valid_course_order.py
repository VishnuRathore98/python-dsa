def find_order(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = [0] * num_courses
    order = []

    def dfs(course):
        if state[course] == 1:
            return False
        if state[course] == 2:
            return True

        state[course] = 1
        for prereq in graph[course]:
            if not dfs(prereq):
                return False
        state[course] = 2
        order.append(course)   # add AFTER all prereqs are processed
        return True

    for course in range(num_courses):
        if not dfs(course):
            return []   # cycle -> no valid order

    return order

print(find_order(4, [[1,0],[2,0],[3,1],[3,2]]))   # [0, 1, 2, 3] (valid order)
