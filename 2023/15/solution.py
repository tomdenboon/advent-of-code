import functools

def hash(s: str):
    return functools.reduce(lambda v, c: ((v + ord(c)) * 17)%256, s, 0)

def part_one(input_str: str):
    return sum([hash(s) for s in input_str.split(",")])

def find_label(label, boxes):
    for i, (l, _) in enumerate(boxes[hash(label)]):
        if l == label:
            return i
    return -1
        
def part_two(input_str: str):
    boxes = [ [] for _ in range(256)]
    for operation in input_str.split(","):
        if '=' in operation:
            label, focal_length = operation.split('=')
            if (i := find_label(label, boxes)) != -1:
                boxes[hash(label)][i] = (label, int(focal_length))
            else:
                boxes[hash(label)].append((label, int(focal_length)))
        else:
            label = operation[:-1]
            if (i := find_label(label, boxes)) != -1:
                boxes[hash(label)].pop(i)

    return sum([focal_length * (i + 1) * (j + 1) for i, box in enumerate(boxes) for j, (_, focal_length) in enumerate(box)])
