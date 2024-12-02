def solve(numbers: list[int]) -> int:
    isAscending = True
    isDescending = True
    for i in range(0, len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if abs(diff) < 0 or abs(diff) > 3:
            isDescending = False
            isAscending = False
        if diff <= 0:
            isAscending = False
        if diff >= 0:
            isDescending = False
    if isAscending or isDescending:
        return 1
    return 0

def part_one(input_str: str):
    return sum([solve([int(x) for x in line.split()]) for line in input_str.split("\n")])
        
def part_two(input_str: str):
    score = 0
    for line in input_str.split("\n"):
        numbers = [int(x) for x in line.split()]
        for i in range(1, len(numbers) + 1):
            nums = numbers[:i-1] + numbers[i:]
            solved = solve(nums)
            if solved == 1:
                score += 1
                break
    
    return score
