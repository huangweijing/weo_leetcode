from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        item_list = sorted(cnt.items(), key=lambda x: (x[1], -x[0]))
        ans = []
        for k, v in item_list:
            ans.extend([k] * v)
        return ans

r = Solution().frequencySort([1, 1, 1, 2])
print(r)
