octopus = []


def octopus_flashbanger():
    is_synced = True
    for i in range(len(octopus)):
        for j in range(len(octopus[i])):
            octopus[i][j] = octopus[i][j] % 10
            if octopus[i][j] != 0:
                is_synced = False
    return is_synced


def add(i, j):
    if 0 <= i < len(octopus) and 0 <= j < len(octopus[i]) and octopus[i][j] <= 9:
        octopus[i][j] += 1
        if octopus[i][j] > 9:
            return 1 + add(i+1, j) + add(i+1, j+1) + add(i+1, j-1) + add(i-1, j) + add(i-1, j+1) + add(i-1, j-1) + add(i, j+1) + add(i, j-1)
    return 0


file = open('input')
for line in file:
    line = line.strip()
    octopus.append([int(c) for c in line])

flash = 0
is_synced = False
step = 0
while not is_synced:
    for i in range(len(octopus)):
        for j in range(len(octopus[i])):
            flash += add(i, j)
    is_synced = octopus_flashbanger()
    step += 1
    if step == 100:
        print(flash)
print(step)
