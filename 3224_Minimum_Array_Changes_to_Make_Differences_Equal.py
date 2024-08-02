from typing import List
import bisect
from collections import Counter
import math

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        arr = []
        diff_cnt = Counter()
        for i in range(len(nums) // 2):
            diff = abs(nums[-1 - i] - nums[i])
            # we have to change both nums if max + diff > k and min - diff < 0
            # which means min < diff and diff > k - max => diff > max(k - max, min)
            threshold = max(k - min(nums[-1 - i], nums[i]), max(nums[-1 - i], nums[i]))
            diff_cnt[diff] += 1
            arr.append(threshold)
        arr.sort()
        ans = math.inf
        for key, cnt in diff_cnt.items():
            idx = bisect.bisect_left(arr, key)
            ans = min(ans, idx * 2 + (len(arr) - idx) - cnt)
        return ans


data = [
[9,2,7,7,8,9,1,5,1,9,4,9,4,7]
, 9
]
r = Solution().minChanges(*data)
print(r)