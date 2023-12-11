import math

def parse_input(I: str):
    I, graph = I.split("\n\n")
    G = {}
    for line in graph.split("\n"):
        node, children = line.split(" = ")
        l, r = children[1:-1].split(", ")
        G[node] = (l, r)
    return I, G

def solve(I, G, N, predicate):
    steps = 0
    while predicate(N):
        N = G[N][0] if I[steps%len(I)] == 'L' else G[N][1]
        steps += 1
    return steps

def part_one(input_as_string: str):
    I, G = parse_input(input_as_string)
    return solve(I, G, "AAA", lambda N: N != 'ZZZ')

def part_two(input_as_string: str):
    I, G = parse_input(input_as_string)
    R = 1
    for N in [N for N in G if N[-1] == 'A']:
        R = math.lcm(R, solve(I, G, N, lambda N: N[-1] != 'Z'))
    return R
