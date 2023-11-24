file = open('input')

depth = 0
right = 0
for line in file:
    tokens = line.split(' ')
    movement = tokens[0]
    amount = int(tokens[1])
    if movement == 'forward':
        right += amount
    elif movement == 'up':
        depth -= amount
    elif movement == 'down':
        depth += amount
print(depth * right)
