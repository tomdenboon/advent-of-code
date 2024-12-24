def part_one(input_str: str):
    updates, rule_order = parse_input(input_str)

    sum = 0 
    for update in updates:
        new_update = [0] * len(update)
        for n in update:
            new_update[len([x for x in rule_order[n] if x in update])] = n
        
        if new_update == update:
            sum += new_update[len(new_update)//2]

    return sum

def parse_input(input_str):
    rules, updates = input_str.split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

    rule_order = {}
    for (before, after) in rules:
        if before not in rule_order:
            rule_order[before] = []
        if after not in rule_order:
            rule_order[after] = []
        rule_order[after].append(before)
    
    return updates, rule_order


        
def part_two(input_str: str):
    updates, rule_order = parse_input(input_str)

    sum = 0 
    for update in updates:
        new_update = [0] * len(update)
        for n in update:
            new_update[len([x for x in rule_order[n] if x in update])] = n
        
        if new_update != update:
            sum += new_update[len(new_update)//2]

    return sum

