from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_cnt = Counter(nums)
        max_cnt = num_cnt.most_common(1)[0][1]
        ans = 0
        for num, cnt in num_cnt.items():
            if cnt == max_cnt:
                ans += cnt
        return ans

# c = Counter([1, 2, 2, 1])
# print(c.most_common(2)[0][1])




