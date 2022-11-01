from typing import List
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt = Counter(nums[: k])
        for i, num in enumerate(nums):
            if i + k < len(nums):
                cnt[nums[i + k]] += 1
            if i - k - 1 >= 0:
                cnt[nums[i - k - 1]] -= 1
            if cnt[num] > 1:
                return True
        return False


