import re

def parse_line(line: str):
    return list(map(int, re.findall(r'\d+', line)))

def solve(A, B, C, ins): 
    def combo(op):
        if op == 4:
            return A
        if op == 5:
            return B
        if op == 6:
            return C
        return op

    p = 0
    O = []
    while p < len(ins): 
        o = ins[p]
        l = ins[p + 1]
        if o == 0:
            A = A // 2 ** combo(l)
        if o == 1:
            B = B ^ l
        if o == 2:
            B = combo(l) % 8
        if o == 3 and A != 0:
            p = l
        else:
            p += 2
        if o == 4:
            B = B ^ C
        if o == 5:
            O.append(combo(l) % 8)
        if o == 6:
            B = A // 2 ** combo(l)
        if o == 7:
            C = A // 2 ** combo(l)
    return O

def part_one(input_str: str):
    A, B, C, _, ins = [parse_line(line) for line in input_str.splitlines()]
    return ",".join(map(str,solve(A[0], B[0], C[0], ins)))
        
def part_two(input_str: str):
    _, B, C, _, ins = [parse_line(line) for line in input_str.splitlines()]

    def rec(A, level):
        if level == len(ins):
            return A
        A = A << 3
        for i in range(8):
            new_ins = solve(A + i, B, C, ins)
            if ins[-level - 1:] == new_ins:
                result = rec(A + i, level + 1)
                if result is not None:
                    return result
        return None

    return rec(0, 0)
