import math


def perform_instruction(workflows, part, instruction):
    if instruction == "A":
        return sum(part.values())
    elif instruction == "R":
        return 0
    for new_instruction, operation in workflows[instruction]:
        if operation is None:
            return perform_instruction(workflows, part, new_instruction)
        else:
            (part_key, op, val) = operation
            if op == "<" and part[part_key] < val:
                return perform_instruction(workflows, part, new_instruction)
            if op == ">" and part[part_key] > val:
                return perform_instruction(workflows, part, new_instruction)


def perform_instruction2(workflows, part, instruction):
    if instruction == "A":
        return math.prod([t[1] - t[0] for t in part.values()])
    elif instruction == "R":
        return 0
    total = 0
    for new_instruction, operation in workflows[instruction]:
        if operation is None:
            total += perform_instruction2(workflows, part, new_instruction)
        else:
            part_key, op, val = operation
            lower, upper = part[part_key]
            if op == "<" and lower < val:
                new_part = part.copy()
                new_part[part_key] = (lower, min(val, upper))
                continue_part = part.copy()
                continue_part[part_key] = (val, upper)
                part = continue_part
                total += perform_instruction2(workflows, new_part, new_instruction)
            elif op == ">" and upper > val:
                new_part = part.copy()
                new_part[part_key] = (max(val, lower) + 1, upper)
                continue_part = part.copy()
                continue_part[part_key] = (lower, val + 1)
                part = continue_part
                total += perform_instruction2(workflows, new_part, new_instruction)
            if part[part_key][0] >= part[part_key][1]:
                break
    return total


def parse(x):
    instructions = [instruction.split(":") for instruction in x[1].split(",")]
    instructions = [
        (
            instruction[1],
            (instruction[0][0], instruction[0][1], int(instruction[0][2:])),
        )
        if len(instruction) > 1
        else (instruction[0], None)
        for instruction in instructions
    ]
    return (x[0], instructions)


def parse_input(input_str: str):
    workflows, parts = [x.splitlines() for x in input_str.split("\n\n")]
    workflows = dict([parse(workflow[:-1].split("{")) for workflow in workflows])
    parts = [[part.split("=") for part in part[1:-1].split(",")] for part in parts]
    parts = [dict([(part[0], int(part[1])) for part in part]) for part in parts]
    return (workflows, parts)


def part_one(input_str: str):
    workflows, parts = parse_input(input_str)
    return sum(
        [
            perform_instruction(
                workflows,
                part,
                "in",
            )
            for part in parts
        ]
    )


def part_two(input_str: str):
    workflows, _ = parse_input(input_str)
    return perform_instruction2(
        workflows,
        {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)},
        "in",
    )
