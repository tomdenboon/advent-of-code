OPS = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "||": lambda x, y: int(str(x) + str(y)),
}

def solve(numbers, target, operators):
    def recurse(i, current):
        if current > target:
            return 0
        if i == len(numbers):
            return target if current == target else 0
        for operation in operators:
            if result := recurse(i + 1, OPS[operation](current, numbers[i])):
                return result
        return 0
    return recurse(1, numbers[0])

def parse(line: str):
    result, numbers = line.split(":")
    return int(result), list(map(int, numbers.split()))

def solver(input_str: str, operators):
    return sum(solve(numbers, result, operators) for result, numbers in map(parse, input_str.splitlines()))

def part_one(input_str: str):
    return solver(input_str, ["+", "*",])

def part_two(input_str: str):
    return solver(input_str, ["+", "*", "||"])
