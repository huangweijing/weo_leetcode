from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        half = len(nums) >> 1
        for i in range(half):
            result.append(nums[i])
            result.append(nums[half + i])
        return result

