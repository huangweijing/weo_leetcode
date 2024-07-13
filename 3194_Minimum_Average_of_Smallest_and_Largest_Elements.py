from typing import List
from collections import deque


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = deque(sorted(nums))
        ans = math.inf
        while len(nums) > 0:
            max_num = nums.pop()
            min_num = nums.popleft()
            ans = min(ans, (max_num + min_num) / 2)
        return ans
