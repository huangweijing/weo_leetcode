from typing import List
from collections import deque


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        nums = deque(nums)
        ans = 0
        while len(nums) > 0:
            if len(nums) > 1:
                n1 = nums.popleft()
                n2 = nums.pop()
                ans += int(str(n1) + str(n2))
            else:
                ans += nums.pop()
        return ans

