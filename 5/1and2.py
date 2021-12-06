file = open('input')
lines = {}
for l in file:
    tokens = l.split(' ')
    begin_x, begin_y = [int(x) for x in tokens[0].split(',')]
    end_x, end_y = [int(x) for x in tokens[2].split(',')]
    x_dir = 1
    y_dir = 1
    if begin_y > end_y:
        y_dir = -1
    if begin_x > end_x:
        x_dir = -1
    if begin_x == end_x:
        while begin_y != end_y + y_dir:
            if (begin_x, begin_y) in lines:
                lines[(begin_x, begin_y)] += 1
            else:
                lines[(begin_x, begin_y)] = 1
            begin_y += y_dir
    elif begin_y == end_y:
        while begin_x != end_x + x_dir:
            if (begin_x, begin_y) in lines:
                lines[(begin_x, begin_y)] += 1
            else:
                lines[(begin_x, begin_y)] = 1
            begin_x += x_dir
    elif abs(end_x - begin_x) == abs(end_y - begin_y):
        for i in range(abs(end_x - begin_x) + 1):
            if (begin_x, begin_y) in lines:
                lines[(begin_x, begin_y)] += 1
            else:
                lines[(begin_x, begin_y)] = 1
            begin_x += x_dir
            begin_y += y_dir


score = 0
for x in lines:
    if lines[x] >= 2:
        score += 1
print(score)
