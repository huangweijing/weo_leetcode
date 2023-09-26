import heapq

class MyObj:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        return str(self.val)

print(MyObj(32))

l = [MyObj(3003), MyObj(2999)]
l.sort()
print(list(map(str, l)))

heapq.heapify(l)
heapq.heappush(l, MyObj(7777))
heapq.heappush(l, MyObj(1777))
print(heapq.heappop(l))
print(heapq.heappop(l))
print(heapq.heappop(l))
print(heapq.heappop(l))
