import math
from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        stk = []
        for num in nums:
            total, cnt = num, 1
            while len(stk) > 0 and stk[-1][0] / stk[-1][1] <= total / cnt:
                top = stk.pop()
                total += top[0]
                cnt += top[1]
            stk.append([total, cnt])
        ans = math.ceil(stk[0][0] / stk[0][1])
        return ans

data = [4,7,2,2,9,19,16,0,3,15]
r = Solution().minimizeArrayValue(data)
print(r)