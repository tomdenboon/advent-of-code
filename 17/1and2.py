def yAtStep(step, y_vel):
    y = 0
    while step:
        y += y_vel
        y_vel -= 1
        step -= 1
    return y


def calcPerms(step_possibilities, x_vel, min_y, max_y):
    y_vel = abs(min_y) - 1
    opts = 0
    while y_vel >= min_y:
        for step in step_possibilities:
            y = yAtStep(step, y_vel)
            if min_y <= y <= max_y:
                opts += 1
                break
        y_vel -= 1
    return opts


def calcVelX(min_x, max_x, min_y, max_y):
    opts = 0
    x_vel = 1
    while x_vel <= max_x:
        x = 0
        step = 0
        step_poss = []
        while x <= max_x:
            if x >= min_x:
                step_poss.append(step)
            if x_vel - step <= 0:
                break
            x += x_vel - step
            step += 1
        if min_x <= x_vel * (x_vel+1) / 2 <= max_x:
            step_poss = [i for i in range(step_poss[0], (abs(min_y) + 1) * 2)]
        opts += calcPerms(step_poss, x_vel, min_y, max_y)
        x_vel += 1
    return opts


f = open("input")
l = f.readline().strip()[13:].split(', ')
x1, x2, = [int(x) for x in l[0].split('=')[1].split('..')]
y1, y2, = [int(y) for y in l[1].split('=')[1].split('..')]
opts = calcVelX(x1, x2, y1, y2)
highest = abs(y1) - 1
print(opts)
print(int(highest * (highest + 1) / 2))
