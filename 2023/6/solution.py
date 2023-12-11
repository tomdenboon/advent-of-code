import math

def accelerate(time, distance):
    x_1 = -(-time + math.sqrt(math.pow(time, 2) - 4*distance))/2
    x_2 = -(-time - math.sqrt(math.pow(time, 2) - 4*distance))/2
    return math.ceil(x_2) - math.floor(x_1) - 1

def part_one(input_as_string: str):
    times, distances = [[int(x) for x in i.split() if x.isnumeric()] for i in input_as_string.splitlines()]
    return math.prod(accelerate(time, distance) for (time, distance) in zip(times, distances))
        
def part_two(input_as_string: str):
    times, distances = [int("".join(i.split()[1:])) for i in input_as_string.splitlines()]
    return accelerate(times, distances)