import re

def part_one(input_str: str):
    pattern = r"mul\((\d+),\s*(\d+)\)"
    multiplies = re.findall(pattern, input_str)
    score = 0
    for (a, b) in multiplies:
        score += int(a) * int(b)
    return score

        
def part_two(input_str: str):
    pattern = r"(mul\(\d+,\s*\d+\)|do\(\)|don't\(\))"
    operations = re.findall(pattern, input_str)
    score = 0
    enabled = True
    print(operations)
    for operation in operations:
        if operation == "do()":
            enabled = True
        elif operation == "don't()":
            print(operation)
            enabled = False
        elif enabled:
            a, b = re.findall(r"\d+", operation)
            score += int(a) * int(b)

    return score
