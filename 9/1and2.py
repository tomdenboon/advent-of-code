is_visited = {}


def find_basin_size(grid, i, j):
    if (i, j) in is_visited or i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0 or grid[i][j] == 9:
        return 0
    else:
        is_visited[(i, j)] = True
        size = 1
        size += find_basin_size(grid, i + 1, j)
        size += find_basin_size(grid, i - 1, j)
        size += find_basin_size(grid, i, j + 1)
        size += find_basin_size(grid, i, j - 1)
        return size


file = open('input')
grid = []
for line in file:
    line = line.strip()
    row = []
    print(line)
    for x in line:
        row.append(int(x))
    grid.append(row)

risk_level = 0
big_basins = [0, 0, 0]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        is_low = True
        if i + 1 < len(grid) and grid[i + 1][j] <= grid[i][j]:
            is_low = False
        if i - 1 >= 0 and grid[i - 1][j] <= grid[i][j]:
            is_low = False
        if j + 1 < len(grid[i]) and grid[i][j + 1] <= grid[i][j]:
            is_low = False
        if j - 1 >= 0 and grid[i][j - 1] <= grid[i][j]:
            is_low = False
        if is_low:
            risk_level += 1+grid[i][j]
            size = find_basin_size(grid, i, j)
            if size > big_basins[0]:
                big_basins[0] = size
            big_basins.sort()
print(risk_level)
print(big_basins[0] * big_basins[1] * big_basins[2])
