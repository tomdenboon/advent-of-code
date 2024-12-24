dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def parse(g):
    B = set()
    IB = set()
    for y, line in enumerate(g.splitlines()):
        for x, c in enumerate(line):
            if c == "@":
                P = (x, y)
            if c == "O":
                B.add((x, y))
            if c == "#":
                IB.add((x, y))
    return P, IB, B

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def print_M(P, IB, B):
    max_x = max([x for x, y in IB])
    max_y = max([y for x, y in IB])
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) == P:
                print("@", end="")
            elif (x, y) in B:
                print("[", end="")
            elif (x - 1, y) in B:
                print("]", end="")
            elif (x, y) in IB or (x - 1, y) in IB:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def part_one(input_str: str):
    g, s = input_str.split("\n\n")
    P, IB, B = parse(g)

    for l in s.splitlines():
        for o in l:
            d = dir[0]
            if o == ">":
                d = dir[1]
            if o == "^":
                d = dir[2]
            if o == "<":
                d = dir[3]

            mB = []
            nP = add(P, d)
            next = nP

            while next in B:
                mB.append(next)
                next = add(next, d)

            if not next in IB:
                P = nP
                B.difference_update(mB)
                B.update([add(b, d) for b in mB])

    return sum([100*b[1] + b[0]  for b in B])

def scale(c):
    return (c[0] * 2, c[1])
        
def part_two(input_str: str):
    g, s = input_str.split("\n\n")
    P, IB, B = parse(g)
    P = (P[0] * 2, P[1])
    IB = set(map(scale, IB))
    B = set(map(scale, B))

    for l in s.splitlines():
        for o in l:
            d = dir[0]
            if o == ">":
                d = dir[1]
            if o == "^":
                d = dir[2]
            if o == "<":
                d = dir[3]

            nP = add(P, d)
            mB = set()
            N = set([nP])
            space = True
            while len(N) > 0:
                Nt = set()
                for n in N:
                    for nn in [n, (n[0] - 1, n[1])]:
                        if nn in B and nn not in mB:
                            mB.add(nn)
                            Nt.add(add(nn, d))
                            Nt.add(add(add(nn, d), (1, 0)))
                        if nn in IB:
                            space = False
                N = Nt

            if space:
                P = nP
                B.difference_update(mB)
                B.update([add(b, d) for b in mB])
    
    return sum([100*b[1] + b[0]  for b in B])
