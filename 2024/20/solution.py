import heapq

def part_one(input_str: str):
    M, C = {}, {}
    S, E = None, None
    for y, l in enumerate(input_str.split("\n")):
        for x, c in enumerate(l):
            if c != "#":
                M[(x, y)] = c
            else:
                C[(x, y)] = "#"
            if c == "S":
                S = (x, y)
            if c == "E":
                E = (x, y)
    
    Q = [(S, 0)]
    V = {}
    while Q:
        point, score = heapq.heappop(Q)
        V[point] = score
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_point = (point[0] + d[0], point[1] + d[1])
            if next_point not in V and next_point in M:
                heapq.heappush(Q, (next_point, score + 1))


    def cheat(point):
        Q = [(point, 0)]
        found_points = {}
        V = {}
        while Q:
            point, score = heapq.heappop(Q)
            V[point] = score
            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_point = (point[0] + d[0], point[1] + d[1])
                if next_point in M and next_point not in found_points:
                    found_points[next_point] = score + 1
                if next_point not in V and next_point in C and score < 20:
                    heapq.heappush(Q, (next_point, score + 1))
        return found_points


    cheats = {}
    for p in pv:
        points = cheat(p)
        for p2 in points:
            cheats.setdefault(pv[p] - pv[p2], 0)
            cheats[pv[p] - pv[p2]] += 1

    print(cheats)
    return 0
    
        
        
def part_two(input_str: str):
    return 0
