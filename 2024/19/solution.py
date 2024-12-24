def part_one(input_str: str):
    T, S = input_str.split("\n\n")
    T = set(T.split(", "))
    no_solution = set()
    def solve(s):
        if s in no_solution:
            return 0
        if s == "":
            return 1
        
        for t in T:
            if s.startswith(t):
                if i := solve(s[len(t):]):
                    return i
        
        no_solution.add(s)
        return 0
    return sum([solve(s) for s in S.split("\n")])
        
def part_two(input_str: str):
    T, S = input_str.split("\n\n")
    T = set(T.split(", "))
    solution = {}

    def solve(s):
        if s == "":
            return 1
        if s not in solution:
            solution[s] = sum([solve(s[len(t):]) for t in T if s.startswith(t)])
        return solution[s]


    return sum([solve(s) for s in S.split("\n")])