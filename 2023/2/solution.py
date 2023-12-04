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

def score_part2(line):
    colors = {'red':0, 'green':0, 'blue':0}
    for count, color in re.findall(r'(\d+) (\w+)', line):
        colors[color] = max(colors[color], int(count))
    return math.prod(colors.values())

def part_one():
    print(sum(map(score_part1, )))
        
def part_two():
    print(sum(map(score_part2, open(sys.argv[1]))))
    
import math, re, sys
part_one()
part_two()