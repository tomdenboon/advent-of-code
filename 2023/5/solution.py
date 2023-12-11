def part_one(input_as_string: str): 
    source_destination = []
    split_input = input_as_string.split("\n\n")
    source = [int(x) for x in split_input[0].split()[1:]]
    for blob in split_input[1:]:
        source_destination.append([[int(x) for x in line.split()] for line in blob.split("\n")[1:]])
    
    for m in source_destination:
        destination = []
        for i, s in enumerate(source):
            for (start_d, start_s, r) in m:
                if start_s <= s < start_s + r:
                    destination.append(start_d + s - start_s)
            if len(destination) == i:
                destination.append(s)
        source = destination
    return min(source)


def part_two(input_as_string: str):
    source_destination = []
    split_input = input_as_string.split("\n\n")
    source = [int(x) for x in split_input[0].split()[1:]]
    source = [(source[i], source[i] + source[i+1]) for i in range(0,len(source), 2)]
    for blob in split_input[1:]:
        source_destination.append([[int(x) for x in line.split()] for line in blob.split("\n")[1:]])
    
    for m in source_destination:
        destination = []
        for (target_left, match_source_left, offset) in m:
            next_source = []
            while source:
                (source_left, source_right) = source.pop()
                match_source_right = match_source_left + offset
                new_source_left = max(source_left, match_source_left)
                new_source_right = min(source_right, match_source_right)
                if new_source_left < new_source_right:
                    o = new_source_left - match_source_left
                    t = new_source_right - new_source_left
                    destination.append((target_left + o, target_left + o + t))
                
                l_remained_right = min(match_source_left, source_right)
                if source_left < l_remained_right:
                    next_source.append((source_left, l_remained_right))

                r_remained_left = max(match_source_right, source_left)
                if r_remained_left < source_right:
                    next_source.append((r_remained_left, source_right))
            source = next_source
        source = destination + source
    return min([s[0] for s in source])