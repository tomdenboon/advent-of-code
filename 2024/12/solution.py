def get_neighbours(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def calculate_perimeter(visited):
    perimeter = 0
    for (x, y) in visited:
        for nx, ny in get_neighbours(x, y):
            if (nx, ny) not in visited:
                perimeter += 1
    return perimeter

def calculate_perimeter_part_two(visited):
    fences = set()
    for (x, y) in visited:
        for nx, ny in get_neighbours(x, y):
            if (nx, ny) not in visited:
                fences.add((x, y, nx - x, ny - y))
    
    calculated = set()
    score = 0
    for (x, y, dx, dy) in fences:
        if (x, y, dx, dy) in calculated:
            continue

        score += 1
        dir = [(0, 1), (0, -1)] if dx != 0 else [(1, 0), (-1, 0)]
        for d in dir:
            i = 1
            while True:
                scaled_coords = (x + i * d[0], y + i * d[1], dx, dy)
                if scaled_coords in fences:
                    calculated.add(scaled_coords)
                    i += 1
                else:
                    break
    return score

def flood_fill(grid, start_x, start_y):
    visited_local = {}
    Q = [(start_x, start_y)]
    while Q:
        x, y = Q.pop()
        if (x, y) in visited_local:
            continue
        visited_local[(x, y)] = True
        for nx, ny in get_neighbours(x, y):
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == grid[start_x][start_y]:
                Q.append((nx, ny))
    return visited_local


def part_one(input_str: str):
    visited = {}
    grid = input_str.splitlines()
    total = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                v = flood_fill(grid, x, y)
                visited.update(v)
                total += len(v) * calculate_perimeter(v)
    return total
        
def part_two(input_str: str):
    visited = {}
    grid = input_str.splitlines()
    total = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                v = flood_fill(grid, x, y)
                visited.update(v)
                total += len(v) * calculate_perimeter_part_two(v)
    return total
