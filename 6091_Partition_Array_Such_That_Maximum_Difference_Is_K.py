from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        group_start = nums[0]
        group_cnt = 1
        for i in range(len(nums)):
            if nums[i] <= group_start + k:
                continue
            else:
                group_start = nums[i]
                group_cnt += 1
        return group_cnt

sol = Solution()
r = sol.partitionArray([2,2,4,5], 0)
print(r)
