from typing import List
from collections import Counter


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()
        for i, num in enumerate(nums):
            cnt[i & 1] += num
        cnt2 = Counter()
        for i, num in enumerate(nums):
            cnt[i & 1] -= num
            if cnt[0] + cnt2[1] == cnt[1] + cnt2[0]:
                ans += 1
            cnt2[i & 1] += num
        return ans


data = [1, 1, 1]
r = Solution().waysToMakeFair(data)
print(r)


        