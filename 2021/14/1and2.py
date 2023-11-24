# dont look at this code.

known_insert = {}
count = {}
insert = {}


def insertPair(pair, steps):
    char_count = {}
    if steps < 0:
        return {}
    if (pair, steps) in known_insert:
        return known_insert[(pair, steps)]
    elif pair in insert:
        char_count[insert[pair]] = 1
        char_count_1 = insertPair(
            pair[0] + insert[pair], steps - 1)
        char_count_2 = insertPair(
            insert[pair] + pair[1], steps - 1)
        for key in char_count_1:
            if key in char_count:
                char_count[key] += char_count_1[key]
            else:
                char_count[key] = char_count_1[key]
        for key in char_count_2:
            if key in char_count:
                char_count[key] += char_count_2[key]
            else:
                char_count[key] = char_count_2[key]
        known_insert[(pair, steps)] = char_count
        return char_count
    else:
        return {}


file = open('input')
polymer = file.readline().strip()
file.readline()
for line in file:
    tokens = line.strip().split(" ")
    insert[tokens[0]] = tokens[2]

char_counts = {}
for c in polymer:
    char_counts[c] = 1
for i in range(1, len(polymer)):
    pair_chars = insertPair(polymer[i-1] + polymer[i], 39)
    for key in pair_chars:
        if key in char_counts:
            char_counts[key] += pair_chars[key]
        else:
            char_counts[key] = pair_chars[key]
print(char_counts)
cnts = list(char_counts.values())
cnts.sort()
print(cnts[-1] - cnts[0])
