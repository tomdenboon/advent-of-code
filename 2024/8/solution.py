def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def in_bounds(coord, bounds):
    return 0 <= coord[0] < bounds[0] and 0 <= coord[1] < bounds[1]

def parse_input(input_str: str):
    grouped_antennas = {}
    lines = input_str.splitlines()
    bounds = (len(lines[0]), len(lines))
    for y, line in enumerate(input_str.splitlines()):
        for x, c in enumerate(line):
            if c != '.':
                grouped_antennas.setdefault(c, []).append((x, y))
    return bounds, grouped_antennas

def part_one(input_str: str):
    bounds, grouped_antennas = parse_input(input_str)
    antinodes = set()

    def add_antinodes(a, b):
        velocity = sub(a, b)
        coord = add(a, velocity)
        if in_bounds(coord, bounds):
            antinodes.add(coord)

    for a, antennas in grouped_antennas.items():
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                add_antinodes(antennas[i], antennas[j])
                add_antinodes(antennas[j], antennas[i])

    return len(antinodes)

        
def part_two(input_str: str):
    bounds, grouped_antennas = parse_input(input_str)
    antinodes = set()

    def add_antinodes(a, b):
        velocity = sub(a, b)
        coord = add(a, velocity)
        while in_bounds(coord, bounds):
            antinodes.add(coord)
            coord = add(coord, velocity)

    for a, antennas in grouped_antennas.items():
        for i in range(len(antennas)):
            antinodes.add(antennas[i])
            for j in range(i + 1, len(antennas)):
                add_antinodes(antennas[i], antennas[j])
                add_antinodes(antennas[j], antennas[i])

    return len(antinodes)
