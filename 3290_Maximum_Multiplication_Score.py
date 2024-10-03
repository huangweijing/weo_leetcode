from typing import List
from functools import cache
import math


class Solution:

    def maxScore(self, a: List[int], b: List[int]) -> int:
        ans = -math.inf
        op = [-math.inf, -math.inf, -math.inf, -math.inf]
        for i, num in enumerate(b):
            new_op = [-math.inf, -math.inf, -math.inf, -math.inf]
            new_op[0] = max(op[0], num * a[0])
            if i >= 1:
                new_op[1] = max(op[1], op[0] + num * a[1])
            if i >= 2:
                new_op[2] = max(op[2], op[1] + num * a[2])
            if i >= 3:
                new_op[3] = max(op[3], op[2] + num * a[3])
            op = new_op
            ans = max(ans, op[3])
        return ans
    

data = [
    [3,2,5,6]
    , [2,-6,4,-5,-3,2,-7]
]
r = Solution().maxScore(*data)
print(r)

