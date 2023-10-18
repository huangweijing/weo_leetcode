from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1, -1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference and abs(i - j) >= indexDifference:
                    return [i, j]
        return ans