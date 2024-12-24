X = 6
Y = 6
B = 12

def solve(corrupted):
    Q = [(0,0,0)]
    visited = set()
    while Q:
        x,y,steps = Q.pop(0)
        if x == X and y == Y:
            return steps
        if x < 0 or y < 0 or x > X or y > Y:
            continue
        if (x,y) in corrupted:
            continue
        if (x,y) in visited:
            continue
        steps += 1
        visited.add((x,y))
        Q.append((x+1,y,steps))
        Q.append((x-1,y,steps))
        Q.append((x,y+1,steps))
        Q.append((x,y-1,steps))
    return None

def part_one(input_str: str):
    corrupted = set()
    for i, line in enumerate(input_str.splitlines()):
        if i == B:
            break
        x,y = map(int, line.split(","))
        corrupted.add((x,y))
    return solve(corrupted)
    
def part_two(input_str: str):
    corrupted = []
    for i, line in enumerate(input_str.splitlines()):
        x,y = map(int, line.split(","))
        corrupted.append((x,y))
    
    for i in range(B, len(corrupted)):
        if solve(set(corrupted[:i])) is None:
            return corrupted[i-1]
