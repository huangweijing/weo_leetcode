from typing import List
import bisect

class Solution:

    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        y_axis_points = [list[int]() for _ in range(101)]
        for rect in rectangles:
            y_axis_points[rect[1]].append(rect[0])

        for row in y_axis_points:
            row.sort()

        ans = []
        for point in points:
            count = 0
            for y in range(point[1], 101):
                row = y_axis_points[y]
                idx = bisect.bisect_left(row, point[0])
                count += len(row) - idx
            ans.append(count)
        return ans

data = [
    [[1, 1], [2, 2], [3, 3]]
    , [[1, 3], [1, 1]]
]
r = Solution().countRectangles(*data)
print(r)
