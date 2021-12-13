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
    for (x, y) in paper.copy():
        if not x < at_x and at_x - (x - at_x) >= 0:
            paper[(at_x - (x - at_x), y)] = True
            del paper[(x, y)]
    return paper


def fold_y(paper, at_y):
    for (x, y) in paper.copy():
        if not (y < at_y) and at_y - (y - at_y) >= 0:
            paper[(x, at_y - (y - at_y))] = True
            del paper[(x, y)]
    return paper


paper = {}
paper_x = 0
paper_y = 0
parse = True
first_solution = True
for line in open('input'):
    if line == '\n':
        parse = False
        continue
    if parse:
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
        if first_solution:
            print(len(paper))
            first_solution = False
print_paper(paper, paper_x, paper_y)
