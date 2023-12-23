from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = 10 ** 9
        ans = -1
        for num in nums:
            if num > min_num:
                ans = max(ans, num - min_num)
            min_num = min(num, min_num)
        return ans


