from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        visited_set = set()
        for i in range(len(nums)):
            if i in visited_set:
                continue
            current_set = set()
            while nums[i] not in current_set:
                current_set.add(nums[i])
                i = nums[i]
            ans = max(ans, len(current_set))
            visited_set = visited_set.union(current_set)
        return ans

