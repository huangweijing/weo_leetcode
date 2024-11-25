from typing import List
from collections import Counter


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pre_sum = 0
        cnt = Counter()
        cnt[pre_sum] += 1
        ans = 0
        for num in nums:
            val =  pre_sum + num - target
            if val in cnt:
                cnt = Counter()
                ans += 1
            pre_sum += num
            cnt[pre_sum] += 1
        return ans
    

data = [
    [1,1,1,1,1]
    , 2
]
r = Solution().maxNonOverlapping(*data)
print(r)

