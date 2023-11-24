file = open('input')
grid = []
points = 0
scores = []
for line in file:
    line = line.strip()
    stack = []
    is_corrupted = False
    print(line)
    for c in line:
        if c == ')':
            if stack.pop() != '(':
                points += 3
                is_corrupted = True
                break
        elif c == ']':
            if stack.pop() != '[':
                points += 57
                is_corrupted = True
                break
        elif c == '}':
            if stack.pop() != '{':
                points += 1197
                is_corrupted = True
                break
        elif c == '>':
            if stack.pop() != '<':
                points += 25137
                is_corrupted = True
                break
        else:
            stack.append(c)
    print(stack)
    if not is_corrupted:
        score = 0
        while(stack):
            c = stack.pop()
            score *= 5
            if c == '(':
                score += 1
            if c == '[':
                score += 2
            if c == '{':
                score += 3
            if c == '<':
                score += 4
        scores.append(score)

print(points)

scores.sort()
print(scores)
print(scores[(int(len(scores)/2))])
