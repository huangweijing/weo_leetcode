from typing import List

class Solution:
    def get_min(self, pos1: list[int], pos2: list[int]) -> int:
        x = abs(pos2[0] - pos1[0])
        y = abs(pos2[1] - pos1[1])
        return max(x, y)

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        for i in range(1, len(points)):
            distance += self.get_min(points[i - 1], points[i])
        return distance
