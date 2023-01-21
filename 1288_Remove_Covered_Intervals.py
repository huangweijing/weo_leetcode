from typing import List
from collections import deque

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = len(intervals)
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j:
                    continue
                if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    ans -= 1
                    break
        return ans