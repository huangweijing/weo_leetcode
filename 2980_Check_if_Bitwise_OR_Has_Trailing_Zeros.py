from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        tz_cnt = 0
        for num in nums:
            if num & 1 == 0:
                tz_cnt += 1
        return tz_cnt >= 2
