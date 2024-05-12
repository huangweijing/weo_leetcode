from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        min_dist = math.inf
        for i, p in enumerate(points):
            if p[0] == x:
                if abs(p[1] - y) < min_dist:
                    ans = i
                    min_dist = abs(p[1] - y)
            elif p[1] == y:
                if abs(p[0] - x) < min_dist:
                    ans = i
                    min_dist = abs(p[0] - x)
        return ans
