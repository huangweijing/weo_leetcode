from typing import List
import bisect

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # points.sort(key=lambda x: x[0])
        result = []
        for query in queries:
            x = query[0]
            y = query[1]
            r = query[2]
            n = 0
            for point in points:
                if (point[0] - x) ** 2 + (point[1] - y) ** 2 <= r ** 2:
                    n += 1
            result.append(n)
        return result
