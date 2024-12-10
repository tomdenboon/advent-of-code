def solve(grid, s_i, s_j):
    visited = set()
    
    def recursion(i, j, curr):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != curr or (i, j) in visited:
            return 0
        
        if grid[i][j] == '9':
            visited.add((i, j))
            return 1
        
        curr = str(int(grid[i][j]) + 1)

        return recursion(i-1, j, curr) + recursion(i+1, j, curr) + recursion(i, j-1, curr)  + recursion(i, j+1, curr)
    return recursion(s_i, s_j, "0")


    return len(visited)

def part_one(input_str: str):
    grid = input_str.splitlines()
    sum = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            sum += solve(grid, i, j)
    return sum

def solve2(grid, s_i, s_j):
    def recursion(i, j, curr):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != curr:
            return 0
        
        if grid[i][j] == '9':
            return 1
        
        curr = str(int(grid[i][j]) + 1)

        return recursion(i-1, j, curr) + recursion(i+1, j, curr) + recursion(i, j-1, curr)  + recursion(i, j+1, curr)
    return recursion(s_i, s_j, "0")

def part_one(input_str: str):
    grid = input_str.splitlines()
    sum = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            sum += solve(grid, i, j)
    return sum
        
def part_two(input_str: str):
    grid = input_str.splitlines()
    sum = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            sum += solve2(grid, i, j)
    return sum
