def score2(val):
    sum = 0
    for i in range(1, val+1):
        sum += i
    return sum


file = open('input')
v = [int(x) for x in file.readline().split(',')]
v.sort()
median = v[int(len(v)/2)]
mean = int(sum(v)/len(v))
fuel1 = 0
fuel2 = 0
for val in v:
    fuel1 += abs(val - median)
    fuel2 += score2(abs(val-mean))
print(fuel1)
print(fuel2)
