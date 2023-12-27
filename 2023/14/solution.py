def part_one(input_str: str):
    grid = [list(line) for line in input_str.splitlines()]
    
    load = 0
    for j in range(len(grid[0])):
        rocks = 0
        for i in range(len(grid)):
            if grid[i][j] == 'O':
                rocks += 1
            elif grid[i][j] == '#':
                load += sum([len(grid) - i - o for o in range(rocks)])
                rocks = 0
        load += sum([len(grid) - i - o for o in range(rocks)])
    return load
        

        


def part_two(input_str: str):
    return 0
