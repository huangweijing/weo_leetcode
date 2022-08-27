from sortedcontainers import SortedSet

d = OrderedDict()
d[2] = 3
d[8] = 8
d[21] = 12
d = OrderedDict(d)

while len(d) > 0:
    print(d.popitem(False))

print(list(d.keys()))