from typing import List
from collections import deque
import bisect

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result = [0] * len(heights)
        stack = deque()
        for i in range(len(heights) - 1, -1, -1):
            while len(stack) > 0 and heights[i] >= stack[0]:
                stack.popleft()
            stack.appendleft(heights[i])
            if i == 0:
                break
            if len(stack) > 0 and stack[-1] > heights[i - 1]:
                idx = bisect.bisect_left(stack, heights[i - 1])
                result[i - 1] = idx + 1
            else:
                result[i - 1] = len(stack)
            # print(f"stack={stack}, heights[i - 1]={heights[i - 1]}, idx={idx}")
        return result

data_heights = [5,1,2,3,10]
print(data_heights)
r = Solution().canSeePersonsCount(data_heights)
print(r)


