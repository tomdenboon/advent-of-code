def part_one(input_str: str):
    rules, updates = input_str.split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

    def check_update(update):
        for (before, after) in rules:
            before_i = -1
            after_i = -1
            for i, n in enumerate(update):
                if n == before:
                    before_i = i
                if n == after:
                    after_i = i
            
            if before_i != -1 and after_i != -1:
                if after_i < before_i:
                    return 0
        return update[len(update)//2]

    return sum([check_update(update) for update in updates])
        
def part_two(input_str: str):
    rules, updates = input_str.split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

    def construct_correct(update):
        new_update = []
        for u in update:
            new_update



    def check_update(update):
        for (before, after) in rules:
            before_i = -1
            after_i = -1
            for i, n in enumerate(update):
                if n == before:
                    before_i = i
                if n == after:
                    after_i = i
            
            if before_i != -1 and after_i != -1:
                if after_i < before_i:
                    return construct_correct(update)
        return 0

    return sum([check_update(update) for update in updates])
