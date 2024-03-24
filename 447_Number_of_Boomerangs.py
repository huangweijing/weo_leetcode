from typing import List
from collections import Counter


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i, p1 in enumerate(points):
            dist_cnt = Counter()
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                distance = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
                dist_cnt[distance] += 1
            for val in dist_cnt:
                ans += int(val - 1)
        return ans


data = [[0,0],[1,0],[2,0]]
r = Solution().numberOfBoomerangs(data)
print(r)


