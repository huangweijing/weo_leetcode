import numpy as np
from typing import List
from collections import Counter
from fractions import Fraction

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        cnt = Counter()
        for i in range(len(points)):
            added = set[str]()
            for j in range(len(points)):
                if i == j:
                    continue
                p1 = points[i]
                p2 = points[j]
                # print(p1, p2)
                if p1[0] - p2[0] == 0:
                    key = "*|" + str(p1[0])
                    if key not in added:
                        cnt[key] += 1
                        added.add(key)
                else:
                    slope = Fraction((p1[1] - p2[1]), (p1[0] - p2[0]))
                    # slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
                    c = p1[1] - slope * p1[0]
                    # if slope < 0:
                    #     key = str(-slope) + "|" + str(-c)
                    if slope == 0:
                        key = str(0.0) + "|" + str(c)
                    else:
                        key = str(slope) + "|" + str(c)
                    if key not in added:
                        cnt[key] += 1
                        added.add(key)
                # print(p1, p2, cnt)
        return cnt.most_common()[0][1]

r = Solution().maxPoints([[0,0],[1,-1],[1,1]])
print(r)

print(Fraction(6, 4) * 3)