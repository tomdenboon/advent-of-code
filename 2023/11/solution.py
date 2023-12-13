def distance(a, b, L, weight):
    d_a = b - a
    distance = 0
    o = -1 if d_a < 0 else 1
    for d in range(o, d_a + o, o):
        distance += weight if a + d in L else 1
    return distance

def solve(input_str: str, weight):
    I = [list(line.strip()) for line in input_str.splitlines()]
    G = [(i, j) for i in range(len(I)) for j in range(len(I[i])) if I[i][j] == "#"]
    R = [i for i in range(len(I)) if all(I[i][j] == "." for j in range(len(I[i])))]
    C = [i for i in range(len(I[0])) if all(I[j][i] == "." for j in range(len(I)))]

    total = 0
    for i in range(len(G)):
        for j in range(i + 1, len(G)):
            total += distance(G[i][0], G[j][0], R, weight)
            total += distance(G[i][1], G[j][1], C, weight)
    return total

def part_one(input_str: str):
    return solve(input_str, 2)
        
def part_two(input_str: str):
    return solve(input_str, 1000000)