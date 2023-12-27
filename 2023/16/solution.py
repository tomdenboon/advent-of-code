def out_of_bounds(grid, pos):
    return pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0])

def new_directions(point, direction):
    match(point):
        case ".":
            return [direction]
        case "|":
            d = [(1, 0), (-1, 0)]

            if direction in d:
                return [direction]
            else:
                return d
        case "-":
            d = [(0, 1), (0, -1)]

            if direction in d:
                return [direction]
            else:
                return d
        case "/":
            return [(-direction[1], -direction[0])];
        case "\\":
            return [(direction[1], direction[0])];

def solve(grid, start):
    visited = set()
    stack = [start]
    while stack:
        n = stack.pop()
        pos, direction = n

        if n in visited or out_of_bounds(grid, pos):
            continue
        
        visited.add(n)
        stack += [((pos[0] + d[0], pos[1] + d[1]), d) for d in new_directions(grid[pos[0]][pos[1]], direction)]
    return len({p[0] for p in visited})

def part_one(input_str: str):
    grid = [list(line) for line in input_str.splitlines()]
    return solve(grid, ((0, 0), (0, 1)))
        
def part_two(input_str: str):
    grid = [list(line) for line in input_str.splitlines()]
    max_score = 0
    for i in range(len(grid)):
        for start in [((i, 0), (0, 1)), ((i, len(grid[i]) - 1), (0, -1))]:
            max_score = max(max_score, solve(grid, start))

    for j in range(len(grid[0])):
        for start in [((0, j), (1, 0)), ((len(grid) - 1, j), (-1, 0))]:
            max_score = max(max_score, solve(grid, start))
    return max_score
