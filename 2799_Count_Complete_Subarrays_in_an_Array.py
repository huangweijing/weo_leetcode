from typing import List
from collections import Counter


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        num_cnt = Counter(nums)
        ans = 0
        for i in range(len(nums)):
            tmp_cnt = Counter()
            for j in range(i, len(nums)):
                tmp_cnt[nums[j]] += 1
                if len(num_cnt) == len(tmp_cnt):
                    ans += 1
        return ans