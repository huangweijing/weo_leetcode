from typing import List
from collections import Counter


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        cnt = Counter()
        ans = 0
        while right < len(nums):
            cnt[nums[right]] += 1
            while left < right and cnt[nums[right]] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
