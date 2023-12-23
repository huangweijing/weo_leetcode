from typing import List
from collections import Counter
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cnt = []
        ans = 0
        for num in nums:
            idx = bisect.bisect_left(cnt, num)
            if idx == len(cnt):
                cnt.append(num)
            else:
                cnt[idx] = num
            ans = max(ans, idx + 1)
            # print(cnt)
        return ans


data = [7,7,7,7,7,7,7]
r = Solution().lengthOfLIS(data)
print(r)

