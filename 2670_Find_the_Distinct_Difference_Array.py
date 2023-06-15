from typing import List
from collections import Counter

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix_cnt = Counter()
        suffix_cnt = Counter(nums)
        ans = []
        for i in range(len(nums)):
            prefix_cnt[nums[i]] += 1
            suffix_cnt[nums[i]] -= 1
            if suffix_cnt[nums[i]] == 0:
                del suffix_cnt[nums[i]]
            ans.append(len(prefix_cnt) - len(suffix_cnt))
        return ans