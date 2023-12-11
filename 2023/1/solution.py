def prepare_line(line):
    translation = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }

    for key in translation:
        line = line.replace(key, translation[key])  
    return line


def part_one(input_as_string: str):
    score = 0
    for line in input_as_string.splitlines():
        digit_line = [int(c) for c in line if c.isnumeric()]
        score += digit_line[0] * 10 + digit_line[-1]
    return score

def part_two(input_as_string: str):
    score = 0
    for line in input_as_string.splitlines():
        digit_line = [int(c) for c in prepare_line(line) if c.isnumeric()]
        score += digit_line[0] * 10 + digit_line[-1]
    return score