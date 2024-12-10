def parse(input_str: str):
    empty_partitions = []
    partitions = []
    mul = 0
    for i, c in enumerate(input_str):
        if i%2 == 0:
            partitions.append([ int(c), mul ])
        else:
            empty_partitions.append([ int(c), mul ])
        mul += int(c)
    return partitions, empty_partitions

def part_one(input_str: str):
    for i in reversed(range(len(partitions))):
        partition = partitions[i]
        for j, empty_partition in enumerate(empty_partitions):
            if partition[1] < empty_partition[1]:
                break;

            if empty_partition[0] > 0:
                for x in range(partition[0]):
                    sum += (mul + x) * i

def part_two(input_str: str):
    partitions, empty_partitions = parse(input_str)
    sum = 0
    for i in reversed(range(len(partitions))):
        partition = partitions[i]
        mul = partition[1]
        for j, empty_partition in enumerate(empty_partitions):
            if partition[1] < empty_partition[1]:
                break;

            if partition[0] <= empty_partition[0]:
                mul = empty_partition[1]
                empty_partitions[j] = (empty_partition[0] - partition[0], empty_partition[1] + partition[0])
                break
        
        for x in range(partition[0]):
            sum += (mul + x) * i

    return sum