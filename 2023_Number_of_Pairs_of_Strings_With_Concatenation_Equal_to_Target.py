from typing import List

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        result = 0
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num + num2 == target:
                    result += 1
        return result