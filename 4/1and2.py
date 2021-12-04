def solve(bingo_card, value_map):
    min_turn = len(value_map)
    for i in range(len(bingo_card)):
        max_row = 0
        max_col = 0
        for j in range(len(bingo_card)):
            if value_map[bingo_card[i][j]] > max_row:
                max_row = value_map[bingo_card[i][j]]
            if value_map[bingo_card[j][i]] > max_col:
                max_col = value_map[bingo_card[j][i]]
        if max_row < min_turn:
            min_turn = max_row
        if max_col < min_turn:
            min_turn = max_col
    return min_turn


def score(bingo_card, end_turn, value_map):
    unmarked_score = 0
    final_number = 0
    for i in range(len(bingo_card)):
        for j in range(len(bingo_card)):
            if value_map[bingo_card[i][j]] > end_turn:
                unmarked_score += bingo_card[i][j]
            elif value_map[bingo_card[i][j]] == end_turn:
                final_number += bingo_card[i][j]
    return unmarked_score * final_number


file = open('input')
value_numbers = {}
val = 1
for x in file.readline().split(','):
    value_numbers[int(x)] = val
    val += 1
file.readline()

losing_bingo_card = []
losing_turn = 0
winning_bingo_card = []
winning_turn = len(value_numbers)
bingo_card = []
for line in file:
    if line == "\n":
        wins_turn = solve(bingo_card, value_numbers)
        if wins_turn < winning_turn:
            winning_turn = wins_turn
            winning_bingo_card = bingo_card.copy()
        if wins_turn > losing_turn:
            losing_turn = wins_turn
            losing_bingo_card = bingo_card.copy()
        bingo_card = []
    else:
        bingo_card.append([int(x) for x in line.strip().split(' ') if x != ''])
wins_turn = solve(bingo_card, value_numbers)
if wins_turn < winning_turn:
    winning_turn = wins_turn
    winning_bingo_card = bingo_card.copy()
if wins_turn > losing_turn:
    losing_turn = wins_turn
    losing_bingo_card = bingo_card.copy()
print(score(winning_bingo_card, winning_turn, value_numbers))
print(score(losing_bingo_card, losing_turn, value_numbers))
