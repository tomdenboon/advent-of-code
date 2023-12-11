def getNeighbours(pipe: str):
    match pipe:
        case "-": return [(0, 1), (0, -1)]
        case "|": return [(1, 0), (-1, 0)]
        case "L": return [(-1, 0), (0, 1)]
        case "J": return [(-1, 0), (0, -1)]
        case "7": return [(1, 0), (0, -1)]
        case "F": return [(1, 0), (0, 1)]
        case "S": return [(1, 0), (0, 1)]
        case ".": return []

def parse_graphs(input_as_string: str):
    M = [[c for c in line.strip()] for line in input_as_string.splitlines()]
    (i, j) = [(i, j) for i in range(len(M)) for j in range(len(M[i])) if M[i][j] == "S"][0]
    V = {}
    Q = [(i, j, 0)]
    while Q:
        N = Q.pop(0)
        if (N[0], N[1]) in V:
            continue
        V[(N[0], N[1])] = N[2]
        for C in getNeighbours(M[N[0]][N[1]]):
            NN = (N[0] + C[0], N[1] + C[1])
            if  NN[0] < 0 or NN[1] < 0 or NN[0] >= len(M) or NN[1] >= len(M[0]):
                continue
            if (-C[0], -C[1]) in getNeighbours(M[NN[0]][NN[1]]):
                Q.append((NN[0], NN[1], N[2] + 1))
    return (V, M)


def part_one(I: str):
    return max(parse_graphs(I)[0].values())

def part_two(I: str):
    V, M = parse_graphs(I)
    n = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if (i, j) in V:
                continue
            inside = False
            for j_2 in range(j, len(M[i])):
                if (i, j_2) in V and (-1, 0) in getNeighbours( M[i][j_2] ):
                    inside = not inside
            if inside:
                n += 1
    return n