from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        ans = []
        while len(cnt) > 0:
            row = []
            for key in list(cnt.keys()):
                row.append(key)
                if cnt[key] > 1:
                    cnt[key] -= 1
                else:
                    del cnt[key]
            ans.append(row)
        return ans
