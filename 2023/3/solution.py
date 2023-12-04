def adjacents(i, start, end):
    return { (i, j) for i in (i - 1, i, i + 1) for j in range(start -1 , end + 1) }

def part_one():
    symbols = {(i, j) for i,line in enumerate(open(sys.argv[1]))
                for j, c in enumerate(line.strip()) if not c.isnumeric() and c != '.'}
    total = 0
    for i,line in enumerate(open(sys.argv[1]).readlines()):
        for match in re.compile(r'(\d+)').finditer(line):
            if adjacents(i, match.start(), match.end()) & symbols:
                total += int(match.group())

    print(total)
        
def part_two():
    symbols = {(i, j): [] for i,line in enumerate(open(sys.argv[1])) 
               for j, c in enumerate(line.strip()) if c == '*'}

    for i,line in enumerate(open(sys.argv[1]).readlines()):
        for match in re.finditer(r'(\d+)', line):
            for symbol in adjacents(i, match.start(), match.end()) & symbols.keys():
                symbols[symbol].append(int(match.group()))

    print(sum([math.prod(points) for points in symbols.values() if len(points) == 2]))

import math, re, sys
part_one()
part_two()