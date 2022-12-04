from sortedcontainers import SortedSet

class SmallestInfiniteSet:

    def __init__(self):
        self.num_set = SortedSet(range(1000, 0, -1), key=lambda x: -x)

    def popSmallest(self) -> int:
        return self.num_set.pop()

    def addBack(self, num: int) -> None:
        self.num_set.add(num)

sis = SmallestInfiniteSet()
print(sis.popSmallest())
print(sis.popSmallest())
print(sis.popSmallest())
sis.addBack(2)
print(sis.popSmallest())