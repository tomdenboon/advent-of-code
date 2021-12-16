def readPacket(bits, i):
    V = int(bits[i] + bits[i + 1] + bits[i + 2], 2)
    T = int(bits[i + 3] + bits[i + 4] + bits[i + 5], 2)
    i += 6
    if T == 4:
        bit_number = ""
        while(bits[i] != '0'):
            i += 1
            for j in range(4):
                bit_number += bits[i]
                i += 1
        i += 1
        for j in range(4):
            bit_number += bits[i]
            i += 1
        return i, int(bit_number, 2), V
    else:
        I = bits[i]
        vals = []
        i += 1
        if I == '1':
            L = ""
            for j in range(11):
                L += bits[i]
                i += 1
            sub_packets = int(L, 2)
            for p in range(sub_packets):
                i, val, version = readPacket(bits, i)
                vals.append(val)
                V += version
        else:
            L = ""
            for j in range(15):
                L += bits[i]
                i += 1
            length_sub_packets = i + int(L, 2)
            vals = []
            while i < length_sub_packets:
                i, val, version = readPacket(bits, i)
                vals.append(val)
                V += version
        if T == 0:
            return i, sum(vals, 0), V
        elif T == 1:
            mul = 1
            for val in vals:
                mul *= val
            return i, mul, V
        elif T == 2:
            return i, min(vals), V
        elif T == 3:
            return i, max(vals), V
        elif T == 5:
            return i, int(vals[0] > vals[1]), V
        elif T == 6:
            return i, int(vals[0] < vals[1]), V
        elif T == 7:
            return i, int(vals[0] == vals[1]), V


bits = ""
for c in open("input").readline():
    if c.isalpha():
        bits += format(int(ord(c) - 55), "b")
    else:
        next_bits = format(int(c), "b")
        while len(next_bits) < 4:
            next_bits = '0' + next_bits
        bits += next_bits
print(bits)
print(readPacket(bits, 0))
