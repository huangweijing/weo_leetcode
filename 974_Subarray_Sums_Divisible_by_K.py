from typing import List
from collections import Counter

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_val = 0
        cnt = Counter()
        for num in nums:
            sum_val += num
            cnt[sum_val % k] += 1
        cnt[0] += 1
        ans = 0
        for key, val in cnt.items():
            if val > 1:
                ans += ((val - 1) * val) >> 1
        return ans

data = [
    [5]
    , 9
]
r = Solution().subarraysDivByK(* data)
print(r)