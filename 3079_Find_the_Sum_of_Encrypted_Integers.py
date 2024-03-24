from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(int(str(max(str(num))) * len(str(num))) for num in nums)
