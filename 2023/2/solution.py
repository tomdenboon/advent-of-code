import math, re, importlib

def score_part1(line: str):
    colors = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    game_id = int(line.strip().split(": ")[0].split(" ")[1])
    for count, color in re.findall(r'(\d+) (\w+)', line):
        if int(count) > colors.get(color):
            return 0
    return game_id

def score_part2(line: str):
    colors = {'red':0, 'green':0, 'blue':0}
    for count, color in re.findall(r'(\d+) (\w+)', line):
        colors[color] = max(colors[color], int(count))
    return math.prod(colors.values())

def part_one(input_as_string: str):
    print(sum(map(score_part1, input_as_string.splitlines())))
        
def part_two(input_as_string: str):
    print(sum(map(score_part2, input_as_string.splitlines())))