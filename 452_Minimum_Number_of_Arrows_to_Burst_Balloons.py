from typing import List
from collections import deque

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key=lambda x: x[0])
        points = deque(points)
        # print(points)
        while len(points) > 0:
            point = points.popleft()
            end = point[1]
            # print(point)
            while len(points) > 0 and points[0][0] <= end:
                pop_point = points.popleft()
                end = min(end, pop_point[1])
            ans += 1
        return ans

data = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
r = Solution().findMinArrowShots(data)
print(r)

