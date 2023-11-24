file = open('input')

count = 0
prev = int(file.readline())
for line in file:
    next = int(line)
    if(next > prev):
        count += 1
    prev = next
print(count)
