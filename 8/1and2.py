file = open('input')
total_sum = 0
for line in file:
    line = line.strip()
    inp, out = line.split('|')
    in_vals = [set(x) for x in inp.strip().split(' ')]
    out_vals = [set(x) for x in out.strip().split(' ')]
    numberList = {}
    for i in range(len(in_vals)):
        if len(in_vals[i]) == 2:
            numberList[1] = in_vals[i]
        if len(in_vals[i]) == 4:
            numberList[4] = in_vals[i]
        if len(in_vals[i]) == 3:
            numberList[7] = in_vals[i]
        if len(in_vals[i]) == 7:
            numberList[8] = in_vals[i]
    for i in range(len(in_vals)):
        if len(in_vals[i]) == 6 and not numberList[7].issubset(in_vals[i]):
            numberList[6] = in_vals[i]
    for i in range(len(in_vals)):
        if len(in_vals[i]) == 5 and in_vals[i].issubset(numberList[6]):
            numberList[5] = in_vals[i]
    for i in range(len(in_vals)):
        if len(in_vals[i]) == 5 and in_vals[i].union(numberList[5]) == numberList[8]:
            numberList[2] = in_vals[i]
    for i in range(len(in_vals)):
        if len(in_vals[i]) == 5 and numberList[5] != in_vals[i] and numberList[2] != in_vals[i]:
            numberList[3] = in_vals[i]
    for i in range(len(in_vals)):
        if len(in_vals[i]) == 6 and (numberList[8] - numberList[5]).issubset(in_vals[i]) and not in_vals[i] == numberList[6]:
            numberList[0] = in_vals[i]
    for i in range(len(in_vals)):
        if len(in_vals[i]) == 6 and numberList[0] != in_vals[i] and numberList[6] != in_vals[i]:
            numberList[9] = in_vals[i]
    sum = ''
    for out in out_vals:
        for k in numberList:
            if numberList[k] == out:
                sum += str(k)
    total_sum += int(sum)
print(total_sum)
