def bitArrayToInteger(arr):
    result = 0
    for i in range(len(arr)):
        index = len(arr) - (i+1)
        if arr[index] == '1':
            result += 2**i
    return result


file = open('input')
hist = [0] * 12
total = 0
for line in file:
    i = 0
    for c in line:
        if c == "1":
            hist[i] += 1
        i += 1
    total += 1

epsilon = []
gamma = []
for bit in hist:
    if bit > total/2:
        epsilon.append('1')
        gamma.append('0')
    elif bit < total/2:
        epsilon.append('0')
        gamma.append('1')
print(bitArrayToInteger(epsilon) * bitArrayToInteger(gamma))
