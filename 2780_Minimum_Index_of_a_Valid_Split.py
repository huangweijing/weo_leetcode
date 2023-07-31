from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cnt = Counter()
        cnt_rev = Counter(nums)
        for i, num in enumerate(nums):
            cnt[num] += 1
            cnt_rev[num] -= 1
            # print(cnt, cnt_rev)
            if cnt[num] * 2 > i + 1 and cnt_rev[num] * 2 > len(nums) - 1 - i:
                return i
        return -1

data = [2,1,3,1,1,1,7,1,2,1]
r = Solution().minimumIndex(data)
print(r)
