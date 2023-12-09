def solve(N):
    if len(N) == 1 or not any(N):
        return N[0]
    return solve([n1 - n2 for  n1, n2 in zip(N[1:], N[:-1]) ]) + N[-1]


def part_one(input_as_string: str):
    L = [line.strip().split() for line in input_as_string.splitlines()]
    S = sum([solve([int(n) for n in line]) for line in L])
    print(S)


        
def part_two(input_as_string: str):
    lines = [line.strip().split() for line in input_as_string.splitlines()]
    lines = [[int(n) for n in line] for line in lines]
    S = sum([solve(l[::-1]) for l in lines])
    print(S)
    
import math, sys, re
input_as_string = open(sys.argv[1]).read()
part_one(input_as_string)
part_two(input_as_string)