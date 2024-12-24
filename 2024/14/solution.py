import re
import time

X=11
Y=7

def parse_line(line: str):
    return list(map(int, re.findall(r'-?\d+', line)))

def has_neighbours(x, y, visualize):
    for (dx, dy) in [(0,1), (1,0), (0,-1), (-1,0), (1, 1),(-1, -1), (-1, 1), (1, -1)]:
        if (x+dx, y+dy) in visualize:
            return 1 * visualize[(x, y)]
    return 0

def solve(input_str: str, t: int):
    grid = {}
    for line in input_str.splitlines():
        px, py, vx, vy = parse_line(line)
        ex = (px + vx * t)%X
        ey = (py + vy * t)%Y
        grid.setdefault((ex,ey), 0) 
        grid[(ex,ey)] += 1
    return grid


def part_one(input_str: str):
    count = [0, 0, 0, 0]
    t=100
    grid = solve(input_str, t)
    mx = X // 2
    my = Y // 2

    for (x, y) in grid:
        if x > mx and y > my:
            count[0] += grid[(x,y)]
        elif x < mx and y > my:
            count[1] += grid[(x,y)]
        elif x > mx and y < my:
            count[2] += grid[(x,y)]
        elif x < mx and y < my:
            count[3] += grid[(x,y)]

    total = 1
    for c in count:
        total *= c
        
    return total
        
def part_two(input_str: str):
    for t in range(0, 10000):
        visualize = solve(input_str, t)
        robots_with_neighbours = sum([has_neighbours(x, y, visualize) for (x, y) in visualize])
        if robots_with_neighbours >= 251:
            for y in range(Y):
                for x in range(X):
                    if (x,y) in visualize:
                        print(visualize[(x,y)], end='')
                    else:
                        print('.', end='')
                print()
            time.sleep(1)
    return None