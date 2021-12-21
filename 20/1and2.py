def get_bit(x, y, image, phase):
    new_bit = ""
    for y_n in [-1, 0, 1]:
        for x_n in [-1, 0, 1]:
            if (x + x_n, y + y_n) in image:
                if image[(x + x_n, y + y_n)] == '#':
                    new_bit += "1"
                else:
                    new_bit += "0"
            elif b[0] == '#':
                if phase % 2:
                    new_bit += "1"
                else:
                    new_bit += "0"
            else:
                new_bit += '0'
    if b[int(new_bit, 2)] == '#':
        return '#'
    else:
        return '.'


f = open("input.txt")
b = [x for x in f.readline().strip()]
f.readline()
image = {}
b_y = [0, 0]
b_x = [0, 0]
for line in f:
    x = 0
    b_x[1] = 0
    for c in line.strip():
        if c == '#':
            image[(b_x[1], b_y[1])] = c
        if c == '.':
            image[(b_x[1], b_y[1])] = c
        b_x[1] += 1
    b_y[1] += 1


b_y[0] -= 5
b_y[1] += 5
b_x[0] -= 5
b_x[1] += 5
cnt = 0
phase = 0
new_image = {}
for _ in range(50):
    cnt += 1
    b_y[0] -= 1
    b_y[1] += 1
    b_x[0] -= 1
    b_x[1] += 1
    for y in range(b_y[0], b_y[1]):
        for x in range(b_x[0], b_x[1]):
            new_image[x, y] = get_bit(x, y, image, phase)
    phase += 1
    image = new_image
    new_image = {}
print(len([1 for x in image if image[x] == '#']))
