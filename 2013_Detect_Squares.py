from collections import defaultdict, Counter
from typing import List


class DetectSquares:

    def __init__(self):
        self.row = defaultdict(lambda: Counter[int]())
        self.col = defaultdict(lambda: Counter[int]())
        

    def add(self, point: List[int]) -> None:
        self.row[point[1]][point[0]] += 1
        self.col[point[0]][point[1]] += 1
        

    def count(self, point: List[int]) -> int:
        ans = 0
        for i, c in self.row[point[1]].items():
            width = abs(point[0] - i)
            if width == 0:
                continue
            if point[1] - width in self.col[point[0]] \
                and point[1] - width in self.col[i]:
                ans += self.col[point[0]][point[1] - width] * self.col[i][point[1] - width] * c
            if point[1] + width in self.col[point[0]] \
                and point[1] + width in self.col[i]:
                ans += self.col[point[0]][point[1] + width] * self.col[i][point[1] + width] * c
        return ans
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)