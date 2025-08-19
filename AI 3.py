from collections import deque

def is_goal(state):
    return state[0] == 2 or state[1] == 2

def get_next_states(state, max_a, max_b):
    a, b = state
    states = []

    
    states.append((max_a, b))
    
    states.append((a, max_b))
    
    states.append((0, b))
    
    states.append((a, 0))
    
    pour = min(a, max_b - b)
    states.append((a - pour, b + pour))
    
    pour = min(b, max_a - a)
    states.append((a + pour, b - pour))

    return states

def bfs(max_a, max_b):
    start = (0, 0)
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        (current, path) = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        if is_goal(current):
            return path

        for next_state in get_next_states(current, max_a, max_b):
            queue.append((next_state, path + [next_state]))

    return None


max_a = 4
max_b = 3


solution = bfs(max_a, max_b)


if solution:
    print("Steps to reach the goal:")
    for step in solution:
        print(f"Jug A: {step[0]}L, Jug B: {step[1]}L")
else:
    print("No solution found.")
