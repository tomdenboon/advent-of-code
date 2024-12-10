def find_starting_pos(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '^':
                return (x, y)
    

def turn_right(direction):
    return (-direction[1], direction[0])

def in_bounds(pos, grid):
    return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def part_one(input_str: str):
    grid = input_str.splitlines()
    pos = find_starting_pos(grid)
    visited = set()
    direction = (0, -1)

    while in_bounds(pos, grid):
        if grid[pos[1]][pos[0]] == '#':
            pos = sub(pos, direction)
            direction = turn_right(direction)
        visited.add(pos)
        pos = add(pos, direction)
    
    return len(visited)


def part_two(input_str: str):
    grid = input_str.splitlines()
    start_pos = find_starting_pos(grid)

    def test_obstruction(pos, obstruction):
        visited = set()
        direction = (0, -1)

        while in_bounds(pos, grid):
            if (pos, direction) in visited:
                return 1

            if grid[pos[1]][pos[0]] == '#' or pos == obstruction:
                pos = sub(pos, direction)
                direction = turn_right(direction)
            visited.add((pos, direction))
            pos = add(pos, direction)
        return 0
    
    total = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            total += test_obstruction(start_pos, (x, y))
        print(str(y) + " / " + str(len(grid)))
    return total
