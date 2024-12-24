import heapq
import re

def cramer(a,b,c,d,e,f):
    det = a * d - b * c
    if det == 0:
        return None, None
    x = (e * d - b * f) // det
    y = (a * f - e * c) // det
    return x, y

def solve(part):
    a, b, p = [list(map(int, re.findall(r'(\d+)', line))) for line in part.split("\n")]
    min_cost = None
    for i in range(101):
            rem_x = p[0] - i * a[0]
            rem_y = p[1] - i * a[1]

            if rem_x % b[0] == 0 and rem_y % b[1] == 0:
                b_x = rem_x // b[0]
                b_y = rem_y // b[1]
                
                if b_x == b_y: 
                    cost = 3 * i + b_x
                    min_cost = min(min_cost, cost) if min_cost is not None else cost

    return 0 if min_cost is None else min_cost

def part_one(input_str: str):
    parts = input_str.split("\n\n")
    sum = 0
    for part in parts:
        sum += solve(part)
    return sum
        
def part_two(input_str: str):
    parts = input_str.split("\n\n")
    sum = 0
    for part in parts:
        a, b, p = [list(map(int, re.findall(r'(\d+)', line))) for line in part.split("\n")]
        p = (p[0] + 10000000000000, p[1] + 10000000000000)
        result = cramer(a[0], b[0], a[1], b[1],  p[0], p[1])
        actual = ( result[0] * a[0] + result[1] * b[0], result[0] * a[1] + result[1] * b[1] )
        if p == actual:
            sum += result[0] * 3 + result[1]
    return sum
