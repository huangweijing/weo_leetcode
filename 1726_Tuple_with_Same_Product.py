from typing import List
from collections import Counter


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnt = Counter()
        ans = 0
        for i, num1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                ans += cnt[num1 * num2] * 8
                cnt[num1 * num2] += 1
        return ans