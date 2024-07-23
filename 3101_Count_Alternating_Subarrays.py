from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        alt_cnt = 0
        last_num = -1
        ans = 0
        for num in nums:
            if last_num == -1 or num != last_num:
                alt_cnt += 1
            else:
                alt_cnt = 1
            last_num = num
            ans += alt_cnt
        return ans
