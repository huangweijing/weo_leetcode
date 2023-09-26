from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        line = [0] * 101
        for num in nums:
            for i in range(num[0], num[1] + 1):
                line[i] = 1
        ans = 0
        for v in line:
            ans += v
        return ans
