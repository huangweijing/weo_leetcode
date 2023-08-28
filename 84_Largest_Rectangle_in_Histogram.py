import datetime
from typing import List
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = []
        size_stk = []
        for height in heights:
            size = 0
            while len(stk) > 0 and stk[-1] > height:
                bar_height = stk.pop()
                size += size_stk.pop()
                ans = max(ans, bar_height * size)
            stk.append(height)
            size_stk.append(size + 1)
        size = 0
        while len(stk) > 0:
            bar_height = stk.pop()
            size += size_stk.pop()
            ans = max(ans, bar_height * size)
        return ans


start = datetime.datetime.now()
sol = Solution()

data = [2,1,5,6,2,3]
r = sol.largestRectangleArea(data)
print(r)
end = datetime.datetime.now()
print(end - start)
# r = sol.largestRectangleArea(data)
# print(r)

