from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = 0
        max_flip = 0
        for i, flip in enumerate(flips, start=1):
            max_flip = max(flip, max_flip)
            if i == max_flip:
                ans += 1
        return ans
