from typing import List
from collections import deque

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1. 按照终了排序
        # 2. 如果要发生了overlap，则删除终了靠后的能够使得剩下的那个相对不容易overlap
        intervals.sort(key=lambda x: [x[1], x[0]])
        q = deque(intervals)
        interval_list = []
        ans = 0
        while len(q) > 0:
            interval = q.popleft()
            if len(interval_list) != 0 and interval_list[-1][1] > interval[0]:
                ans += 1
            else:
                interval_list.append(interval)
        return ans


data = [[1,2],[2,3]]
r = Solution().eraseOverlapIntervals(data)
print(r)
