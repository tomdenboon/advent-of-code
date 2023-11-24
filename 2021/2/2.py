file = open('input')

depth = 0
right = 0
aim = 0
for line in file:
    tokens = line.split(' ')
    movement = tokens[0]
    amount = int(tokens[1])
    if movement == 'forward':
        depth += aim * amount
        right += amount
    elif movement == 'up':
        aim -= amount
    elif movement == 'down':
        aim += amount
print(depth * right)
