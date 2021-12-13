def print_paper(paper, x, y):
    for j in range(y):
        row = ""
        for i in range(x):
            if (i, j) in paper:
                row += "#"
            else:
                row += "."
        print(row)


def fold_x(paper, at_x):
    delete_list = []
    add_list = []
    for (x, y) in paper:
        delete_list.append((x, y))
        if x < at_x:
            add_list.append((x, y))
        elif at_x - (x - at_x) >= 0:
            add_list.append((at_x - (x - at_x), y))
    for (x, y) in delete_list:
        del paper[(x, y)]
    for (x, y) in add_list:
        paper[(x, y)] = True
    return paper


def fold_y(paper, at_y):
    delete_list = []
    add_list = []
    for (x, y) in paper:
        delete_list.append((x, y))
        if y < at_y:
            add_list.append((x, y))
        elif at_y - (y - at_y) >= 0:
            add_list.append((x, at_y - (y - at_y)))
    for (x, y) in delete_list:
        del paper[(x, y)]
    for (x, y) in add_list:
        paper[(x, y)] = True
    return paper


paper = {}
paper_x = 0
paper_y = 0
first = True
for line in open('input'):
    if line == '\n':
        first = False
        continue
    if first:
        x, y = [int(x) for x in line.split(',')]
        paper[(x, y)] = True
    else:
        tokens = line.strip().split('=')
        if tokens[0][-1] == 'x':
            paper_x = int(tokens[1])
            paper = fold_x(paper, paper_x)
        elif tokens[0][-1] == 'y':
            paper_y = int(tokens[1])
            paper = fold_y(paper, paper_y)
print_paper(paper, paper_x, paper_y)
print(len(paper))
