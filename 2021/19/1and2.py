import itertools


def transform(s, td, tf):
    return {(tup[tf[0]] * td[0], tup[tf[1]] * td[1], tup[tf[2]] * td[2])
            for tup in s}


def minus(t1, t2):
    return tuple(x-y for x, y in zip(t1, t2))


def abs_minus(t1, t2):
    return tuple(abs(x-y) for x, y in zip(t1, t2))


def intersect(s1, s2):
    facing = itertools.permutations([0, 1, 2])
    direction = list(itertools.product([-1, 1], repeat=3))
    for tf in facing:
        for td in direction:
            t_s2 = transform(s2, td, tf)
            for t1 in s1:
                for t2 in t_s2:
                    offset = minus(t2, t1)
                    s3 = {minus(t3, offset) for t3 in t_s2}
                    if len(s3 & s1) >= 12:
                        return offset, s3


beacons = set()
scanners = []
file = open("input.txt")
file.readline()
for line in file:
    if line[0] == '\n':
        scanners.append(beacons)
        beacons = set()
        file.readline()
    else:
        beacons.add(tuple([int(x) for x in line.split(",")]))


fin = set(scanners.pop(0))
cnt = 0
offsets = []
while scanners:
    s = scanners.pop(0)
    res = intersect(fin, s)
    if res:
        offset, a = res
        fin = fin.union(a)
        cnt += 1
        offsets.append(offset)
    else:
        scanners.append(s)
print(len(fin))

max = 0
for i in range(len(offsets)):
    for j in range(i + 1, len(offsets)):
        curr = sum(abs_minus(offsets[i], offsets[j]))
        if curr > max:
            max = curr
print(max)
