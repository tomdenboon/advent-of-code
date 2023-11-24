import math
from copy import deepcopy


class Pair:
    def __init__(self, l=None, r=None, left=True, parent=None):
        self.parent = parent
        self.left = left
        self.l = l
        self.r = r

    def magnitude(self):
        m = 0
        if type(self.l) == Pair:
            m += 3*self.l.magnitude()
        else:
            m += 3 * self.l
        if type(self.r) == Pair:
            m += 2*self.r.magnitude()
        else:
            m += 2 * self.r
        return m

    def add(self, p):
        p_pair = Pair(l=self, r=p)
        self.parent = p_pair
        self.left = 1
        p.parent = p_pair
        p.left = 0
        return p_pair

    def add_ln(self, add):
        find_parent = self.parent
        if not self.left:
            while find_parent.left == 0:
                find_parent = find_parent.parent
                if find_parent.parent == None:
                    return
            find_parent = find_parent.parent
        if type(find_parent.r) != Pair:
            find_parent.r += add
        else:
            find_parent = find_parent.r
            while type(find_parent.l) == Pair:
                find_parent = find_parent.l
            find_parent.l += add
        return find_parent

    def add_rn(self, add):
        find_parent = self.parent
        if self.left:
            while find_parent.left == 1:
                find_parent = find_parent.parent
                if find_parent.parent == None:
                    return
            find_parent = find_parent.parent
        if type(find_parent.l) != Pair:
            find_parent.l += add
        else:
            find_parent = find_parent.l
            while type(find_parent.r) == Pair:
                find_parent = find_parent.r
            find_parent.r += add
        return find_parent

    def explode(self, d):
        if type(self.l) == Pair:
            if self.l.explode(d+1):
                return True
        if type(self.l) != Pair and type(self.r) != Pair and d >= 4:
            if self.left:
                self.parent.l = 0
            else:
                self.parent.r = 0
            self.add_rn(self.l)
            self.add_ln(self.r)
            return True
        if type(self.r) == Pair:
            if self.r.explode(d+1):
                return True
        return False

    def split(self):
        if type(self.l) == Pair:
            if self.l.split():
                return True
        if type(self.l) != Pair and self.l >= 10:
            self.l = Pair(int(self.l/2), math.ceil(self.l/2),
                          1, self)
            return True
        elif type(self.r) != Pair and self.r >= 10:
            self.r = Pair(int(self.r/2), math.ceil(self.r/2),
                          0, self)
            return True
        if type(self.r) == Pair:
            if self.r.split():
                return True
        return False

    def solve(self):
        while(1):
            if(self.explode(0)):
                pass
            elif not self.split():
                break


f = open("input.txt")
stack = []
pairs = []
for line in f:
    p = Pair()
    left = True
    for i in range(1, len(line.strip())):
        if line[i] == '[':
            new_p = Pair(parent=p,  left=left)
            if left:
                p.l = new_p
            else:
                p.r = new_p
            left = True
            p = new_p
        elif line[i] == ']' and p.parent:
            p = p.parent
            left = True
        elif line[i].isdecimal():
            if left:
                p.l = int(line[i])
            else:
                p.r = int(line[i])
        elif line[i] == ',':
            left = False
    pairs.append(p)

singular_pair = deepcopy(pairs[0])
for i in range(1, len(pairs)):
    singular_pair = singular_pair.add(deepcopy(pairs[i]))
    singular_pair.solve()
print(singular_pair.magnitude())

largest_magn = 0
for i in range(0, len(pairs)):
    for j in range(i+1, len(pairs)):
        p = deepcopy(pairs[i]).add(deepcopy(pairs[j]))
        p.solve()
        if p.magnitude() > largest_magn:
            largest_magn = p.magnitude()
        p = deepcopy(pairs[j]).add(deepcopy(pairs[i]))
        p.solve()
        if p.magnitude() > largest_magn:
            largest_magn = p.magnitude()
print(largest_magn)
