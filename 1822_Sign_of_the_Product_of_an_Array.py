from typing import List


def signFunc(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            sign *= signFunc(num)
        return sign
