import heapq

def out_of_bounds(grid, pos):
    return pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0])

def solve(grid, get_directions, min_steps=0):
    visited = set()
    queue = [(0, (0, 0), (0, 1), 0)]
    while queue:
        n = heapq.heappop(queue)
        count, pos, direction, steps = n
        
        if pos == (len(grid) - 1, len(grid[0]) - 1) and steps >= min_steps:
            return count
        elif (pos, direction, steps) in visited:
            continue

        visited.add((pos, direction, steps))
        
        for new_direction in get_directions(direction, steps):
            new_pos = (pos[0] + new_direction[0], pos[1] + new_direction[1])
            if out_of_bounds(grid, new_pos):
                continue
            new_count = count + int(grid[new_pos[0]][new_pos[1]])
            new_steps = steps + 1 if direction == new_direction else 1
            heapq.heappush(queue, (new_count, new_pos, new_direction, new_steps))

def get_directions1(direction, steps):
    D = [d for d in [(1, 0), (-1, 0), (0, 1), (0, -1)] if d != (-direction[0], -direction[1])]
    if steps == 3:
        D.remove(direction)
    return D

def get_directions2(direction, steps):
    if steps < 4:
        return [direction]
    D = [d for d in [(1, 0), (-1, 0), (0, 1), (0, -1)] if d != (-direction[0], -direction[1])]
    if steps == 10:
        D.remove(direction)
    return D

def part_one(input_str: str):
    grid = [list(line) for line in input_str.splitlines()]
    return solve(grid, get_directions1)
        
def part_two(input_str: str):
    grid = [list(line) for line in input_str.splitlines()]
    return solve(grid, get_directions2, 4)
