file = open('input')

prev1 = int(file.readline())
prev2 = int(file.readline())
prev3 = int(file.readline())

sum_prev = prev1 + prev2 + prev3
sum_next = 0
count = 0
for line in file:
    prev1 = prev2
    prev2 = prev3
    prev3 = int(line)
    sum_next = prev1 + prev2 + prev3
    if(sum_next > sum_prev):
        count += 1
    sum_prev = sum_next
print(count)
