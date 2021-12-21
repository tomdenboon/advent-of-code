calculated_score = {}


def play(p1, p2, score_p1, score_p2, turn, dice):
    if turn != -1:
        if (turn + 1) % 2:
            p1 = (p1 - 1 + sum(dice)) % 10 + 1
            score_p1 += p1
        else:
            p2 = (p2 - 1 + sum(dice)) % 10 + 1
            score_p2 += p2
    if (p1, p2, score_p1, score_p2, turn % 2) in calculated_score:
        return calculated_score[(p1, p2, score_p1, score_p2, turn % 2)]
    if score_p1 >= 21:
        return (1, 0)
    elif score_p2 >= 21:
        return (0, 1)

    t_w_p1 = t_w_p2 = 0
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                t_w_1 = play(p1, p2, score_p1, score_p2, turn + 1, [i, j, k])
                t_w_p1 += t_w_1[0]
                t_w_p2 += t_w_1[1]
    calculated_score[(p1, p2, score_p1, score_p2, turn % 2)] = [t_w_p1, t_w_p2]

    return (t_w_p1, t_w_p2)


f = open("input.txt")
p1, p2 = [int(l.strip()[-1]) for l in f]

score_p1 = score_p2 = 0
turn = 0
add = 0

print(max(play(p1, p2, score_p1, score_p2, -1, [])))
while score_p1 < 1000 and score_p2 < 1000:
    dice_val = add * 3 + 1 + 2 + 3
    if (turn + 1) % 2:
        p1 = (p1 - 1 + dice_val) % 10 + 1
        score_p1 += p1
    else:
        p2 = (p2 - 1 + dice_val) % 10 + 1
        score_p2 += p2
    turn += 1
    add += 3
print((turn*3) * min(score_p1, score_p2))
