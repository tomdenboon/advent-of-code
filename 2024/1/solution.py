def part_one(input_str: str):
    left, right = parse_input(input_str)
    left.sort()
    right.sort()

    return sum([abs(l - r) for (l, r) in zip(left, right)])
        
def part_two(input_str: str):
    left, right = parse_input(input_str)

    righ_histogram = {}
    for r in right:
        righ_histogram[r] = righ_histogram.get(r, 0) + 1

    return sum([righ_histogram[l] * l for l in left if l in righ_histogram])

def parse_input(input_str):
    left = []
    right = []
    for line in input_str.split("\n"):
        l, r = [int(x) for x in line.split()]
        left.append(l)
        right.append(r)

    return left, right
