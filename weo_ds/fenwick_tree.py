class Fenwick:
    def __init__(self, n):
        sz = 1
        while sz <= n:
            sz *= 2
        self.size = sz
        self.data = [0] * sz

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i
            #i & (~i + 1) is a trick to extract the lowest set bit of i.
i = 130
print(bin(i), bin(i & -i), bin((i & -i) + i))

#
f = Fenwick(30)
f.add(7, 20)
f.add(3, 10)
print(f.data)
print(f.sum(5))
#
