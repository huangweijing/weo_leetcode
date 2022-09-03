from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = 0
        result = []
        for num in nums:
            n <<= 1
            n |= num
            result.append(n % 5 == 0)
        return result

