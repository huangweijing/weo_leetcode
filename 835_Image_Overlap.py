import datetime
from typing import List

class Solution:
    def __init__(self):
        self.start = datetime.datetime.now()

    def print_time(self):
        print(datetime.datetime.now() - self.start)

    def largestOverlap(self, img1: List[List[int]]
                       , img2: List[List[int]]) -> int:
        relative_dict = dict[tuple[int], int]()
        n = len(img1)
        img1_lst, img2_lst = [], []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_lst.append((i, j))
                if img2[i][j] == 1:
                    img2_lst.append((i, j))
        ans = 0
        for pt1 in img1_lst:
            for pt2 in img2_lst:
                key = (pt2[0] - pt1[0], pt2[1] - pt1[1])
                if key not in relative_dict:
                    relative_dict[key] = 0
                relative_dict[key] += 1
                ans = max(ans, relative_dict[key])
        return ans

data = [
  [[1,1,0],[0,1,0],[0,1,0]]
, [[0,0,0],[0,1,1],[0,0,1]]
]

r = Solution().largestOverlap(*data)
print(r)
