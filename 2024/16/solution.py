import heapq

def part_one(input_str: str):
    M = {}
    S, E = None, None
    for y, l in enumerate(input_str.split("\n")):
        for x, c in enumerate(l):
            if c != "#":
                M[(x, y)] = c
            if c == "S":
                S = (x, y)
            if c == "E":
                E = (x, y)
    
    Q = [(0, S, (1, 0))]
    V = {}
    while Q:
        score, point, dir = heapq.heappop(Q)
        if point in V and V[point] + 1000 <= score:
            continue

        if point not in V:
            V[point] = score

        if score < V[point]:
            V[point] = score

        score += 1
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dir[0] == -d[0] and dir[1] == -d[1]:
                continue
            next_point = (point[0] + d[0], point[1] + d[1])
            if next_point in M:
                heapq.heappush(Q, (score + 1000 if dir[0] != d[0] or dir[1] != d[1] else score, next_point, d))

    return V[E]
        
        
def part_two(input_str: str):
    M = {}
    S, E = None, None
    for y, l in enumerate(input_str.split("\n")):
        for x, c in enumerate(l):
            if c != "#":
                M[(x, y)] = c
            if c == "S":
                S = (x, y)
            if c == "E":
                E = (x, y)
    
    Q = [(0, S, (1, 0), [S])]
    V = {}
    min_score = 100000000
    nodes = set()
    while Q:
        score, point, dir, path = heapq.heappop(Q)
        if point in V and V[point] + 1000 < score:
            continue

        if point == E and score <= min_score:
            if score < min_score:
                min_score = score
                nodes.clear()
            for n in path:
                nodes.add(n)

        if point not in V:
            V[point] = score

        if score < V[point]:
            V[point] = score

        score += 1
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dir[0] == -d[0] and dir[1] == -d[1]:
                continue
            next_point = (point[0] + d[0], point[1] + d[1])
            if next_point in M:
                heapq.heappush(Q, (score + 1000 if dir[0] != d[0] or dir[1] != d[1] else score, next_point, d, path + [next_point]))
    return len(nodes)