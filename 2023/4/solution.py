def f(line):
    _, cards = line.strip().split(":")
    card1, card2 = cards.split("|")
    card1_nums = {int(n) for n in card1.split()}
    card2_nums = {int(n) for n in card2.split()}
    return len(card1_nums & card2_nums)

def part_one(input_as_string: str):
    scores = map(f, input_as_string.splitlines())
    print(sum([int(math.pow(2, t - 1)) for t in scores if t > 0]))

        
def part_two(input_as_string: str):
    scores = list(map(f, input_as_string.splitlines()))
    copies = [1 for _ in scores]
    for i, score in enumerate(scores):
        for j in range(i + 1, min(i + score + 1, len(copies))):
            copies[j] += copies[i]
    print(sum(copies))
    
import math, sys
input_as_string = open(sys.argv[1]).read()
part_one(input_as_string)
part_two(input_as_string)