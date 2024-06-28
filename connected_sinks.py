from collections import deque

# Pipe connectivity mapping, indicating the relative coordinates of connected neighbors
pipe_connections = {
    '═': [(-1, 0), (1, 0)],        # left, right
    '║': [(0, 1), (0, -1)],        # up, down
    '╔': [(0, -1), (1, 0)],        # down, right
    '╗': [(0, -1), (-1, 0)],       # down, left
    '╚': [(1, 0), (0, 1)],         # right, up
    '╝': [(-1, 0), (0, 1)],        # left, up
    '╠': [(0, 1), (0, -1), (1, 0)],# up, down, right
    '╣': [(-1, 0), (0, -1), (0, 1)],# left, down, up
    '╦': [(0, -1), (-1, 0), (1, 0)],# down, left, right
    '╩': [(0, 1), (-1, 0), (1, 0)]  # up, left, right
}

# Function to read the input file and create the grid
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

# Function to get neighbors based on the object in the cell
def get_neighbors(x, y, obj):
    if obj in pipe_connections:
        return [(x + dx, y + dy) for dx, dy in pipe_connections[obj]]
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

# Function to validate if the connection between two cells is valid
def is_valid_connection(a, b, grid):
    if b not in grid:
        return False
    a_obj = grid[a]
    b_obj = grid[b]

    # Source or sink can connect to any other pipe or sink
    if a_obj == '*' or a_obj.isupper():
        return True
    
    if b_obj == '*' or b_obj.isupper():
        return True
    
    # Check if 'a' can connect to 'b' and 'b' can connect to 'a'
    if a_obj in pipe_connections:
        possible_a_connections = [(a[0] + dx, a[1] + dy) for dx, dy in pipe_connections[a_obj]]
        if b in possible_a_connections:
            reverse_connections = [(b[0] + dx, b[1] + dy) for dx, dy in pipe_connections[b_obj]]
            if a in reverse_connections:
                return True
    return False

# Function to find all sinks connected to the source
def find_connected_sinks(grid):
    # Find the source position
    source = next(pos for pos, obj in grid.items() if obj == '*')
    queue = deque([source])
    visited = set([source])
    sinks = set()
    
    while queue:
        current = queue.popleft()
        x, y = current
        obj = grid[current]
        
        # If the current object is a sink, add it to the sinks set
        if obj.isupper():
            sinks.add(obj)
        
        # Check all neighbors
        for neighbor in get_neighbors(x, y, obj):
            if neighbor in grid and neighbor not in visited:
                if is_valid_connection(current, neighbor, grid):
                    queue.append(neighbor)
                    visited.add(neighbor)
    
    # Return the sorted list of connected sinks as a string
    return ''.join(sorted(sinks))

# Main function to read the input file and find connected sinks
def connected_sinks(file_path):
    grid = read_input(file_path)
    return find_connected_sinks(grid)

# Program usage:
result = connected_sinks('coding_qual_input.txt')
