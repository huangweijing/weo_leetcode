from typing import List
from collections import deque


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        sum_val = sum(nums)
        acc = 0
        ans = 0
        for num in nums:
            acc += num
            if num == 0:
                if abs(2 * acc - sum_val) == 0:
                    ans += 2
                if abs(2 * acc - sum_val) == 1:
                    ans += 1
        return ans

data = [16,13,10,0,0,0,10,6,7,8,7]
r = Solution().countValidSelections(data)
print(r)
        