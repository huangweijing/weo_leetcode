from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[i] == nums[k] or nums[j] == nums[k]:
                        continue
                    ans += 1
        return ans