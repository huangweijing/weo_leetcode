from typing import List
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        sum_cnt = Counter()
        sum_cnt[0] = 1
        ans = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            ans += sum_cnt[prefix_sum - k]
            sum_cnt[prefix_sum] += 1
        return ans

r = Solution().subarraySum([1, 1, 1], 3)
print(r)
