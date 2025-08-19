import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.zero_pos = board.index(0)

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_neighbors(self):
        neighbors = []
        x, y = divmod(self.zero_pos, 3)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_zero = nx * 3 + ny
                new_board = self.board[:]
                new_board[self.zero_pos], new_board[new_zero] = new_board[new_zero], new_board[self.zero_pos]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    def manhattan_distance(self):
        distance = 0
        for i, val in enumerate(self.board):
            if val == 0:
                continue
            target_x, target_y = divmod(val - 1, 3)
            current_x, current_y = divmod(i, 3)
            distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance

    def __lt__(self, other):
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())

def solve_puzzle(start_board):
    start_state = PuzzleState(start_board)
    frontier = []
    heapq.heappush(frontier, start_state)
    explored = set()

    while frontier:
        current = heapq.heappop(frontier)
        if current.is_goal():
            return reconstruct_path(current)

        explored.add(tuple(current.board))
        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) not in explored:
                heapq.heappush(frontier, neighbor)

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    return path[::-1]


initial_board = [1, 2, 3, 4, 0, 6, 7, 5, 8]  
solution = solve_puzzle(initial_board)

print("Steps to solve the puzzle:")
for step in solution:
    for i in range(0, 9, 3):
        print(step[i:i+3])
    print()
