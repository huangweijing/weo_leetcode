from typing import List
from collections import Counter


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        key_list = sorted(list(cnt.keys()))
        ans = 0
        for i, key in enumerate(key_list):
            ans += cnt[key] * i
        return ans

data = [1,1,2,2,3]
r = Solution().reductionOperations(data)
print(r)