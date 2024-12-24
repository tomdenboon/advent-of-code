from functools import lru_cache 

def solve_stones(stones, depth):
    @lru_cache(None)
    def recurse(n, steps):
        if steps == depth:
            return 1
        if n == 0:
            return recurse(1, steps + 1)
        str_n = str(n)
        if len(str_n)%2 == 0:
            return recurse(int(str_n[:len(str_n)//2]), steps + 1) + recurse(int(str_n[len(str_n)//2:]), steps + 1)
        return recurse(n * 2024, steps + 1)
    
    return sum([recurse(stone, 0) for stone in stones])
    
def part_one(input_str: str):
    return solve_stones(list(map(int, input_str.split())), 25)
        
def part_two(input_str: str):
    return solve_stones(list(map(int, input_str.split())), 75)
