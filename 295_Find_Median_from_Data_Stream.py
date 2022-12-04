from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        sl_len = len(self.sl)
        if sl_len & 1 == 1:
            return self.sl[sl_len >> 1]
        else:
            return (self.sl[(sl_len >> 1) - 1] + self.sl[sl_len >> 1]) / 2

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())