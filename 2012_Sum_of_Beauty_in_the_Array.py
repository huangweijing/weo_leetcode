from typing import List
from collections import deque


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        min_from_right = deque()
        min_val = 10e9
        for num in reversed(nums):
            min_val = min(min_val, num)
            min_from_right.appendleft(min_val)
        max_val = 0
        ans = 0
        for i, num in enumerate(nums):
            if 0 < i < len(nums) - 1:
                if max_val < num < min_from_right[i + 1]:
                    ans += 2
                elif nums[i - 1] < num < nums[i + 1]:
                    ans += 1
            max_val = max(num, max_val)
        return ans
        
        