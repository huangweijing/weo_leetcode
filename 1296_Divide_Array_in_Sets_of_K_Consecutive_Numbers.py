from typing import List
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        cnt = Counter(nums)
        for key in sorted(cnt.keys()):
            while cnt[key] > 0:
                for i in range(k):
                    if cnt[key + i] > 0:
                        cnt[key + i] -= 1
                    else:
                        return False
        return True
        