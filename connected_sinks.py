from collections import deque

# Pipe connectivity mapping
pipe_connections = {
    '═': [(0, -1), (0, 1)],        # left, right
    '║': [(-1, 0), (1, 0)],        # up, down
    '╔': [(1, 0), (0, 1)],         # down, right
    '╗': [(1, 0), (0, -1)],        # down, left
    '╚': [(0, 1), (-1, 0)],        # right, up
    '╝': [(0, -1), (-1, 0)],       # left, up
    '╠': [(0, -1), (1, 0), (0, 1)],# left, down, right
    '╣': [(0, -1), (1, 0), (0, 1)],# left, down, right
    '╦': [(-1, 0), (0, -1), (0, 1)],# up, left, right
    '╩': [(1, 0), (0, -1), (0, 1)] # down, left, right
}

def read_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    grid = {}
    for line in lines:
        parts = line.strip().split()
        obj = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        grid[(x, y)] = obj
    return grid

def get_neighbors(x, y, obj):
    if obj in pipe_connections:
        return [(x+dx, y+dy) for dx, dy in pipe_connections[obj]]
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def is_valid_connection(a, b, grid):
    if b not in grid:
        return False
    a_obj = grid[a]
    b_obj = grid[b]

    if a_obj == '*' or a_obj.isupper():  # Source or sink
        return True
    
    if b_obj == '*' or b_obj.isupper():  # Source or sink
        return True
    
    if a_obj in pipe_connections:
        possible_a_connections = [(a[0] + dx, a[1] + dy) for dx, dy in pipe_connections[a_obj]]
        if b in possible_a_connections:
            reverse_connections = [(b[0] + dx, b[1] + dy) for dx, dy in pipe_connections[b_obj]]
            if a in reverse_connections:
                return True
    return False

def find_connected_sinks(grid):
    source = next(pos for pos, obj in grid.items() if obj == '*')
    queue = deque([source])
    visited = set([source])
    sinks = set()
    
    while queue:
        current = queue.popleft()
        x, y = current
        obj = grid[current]

        print(f"Visiting: {current}, Object: {obj}")  # Debugging print to see the current cell
        
        if obj.isupper():
            sinks.add(obj)
        
        for neighbor in get_neighbors(x, y, obj):
            print(f"Checking neighbor: {neighbor}")  # Debugging print to see the neighbor
            if neighbor in grid and neighbor not in visited:
                if is_valid_connection(current, neighbor, grid):
                    print(f"Valid connection: {current} -> {neighbor}")  # Debugging print for valid connection
                    queue.append(neighbor)
                    visited.add(neighbor)
                else:
                    print(f"Invalid connection: {current} -> {neighbor}")  # Debugging print for invalid connection
    
    return ''.join(sorted(sinks))

def connected_sinks(file_path):
    grid = read_input(file_path)
    print("Grid:", grid)  # Debugging print to see the grid structure
    return find_connected_sinks(grid)

# Example usage:
# result = connected_sinks('coding_qual_input.txt')
result = connected_sinks('example_pipe_system.txt')
print("Result:", result)
