from typing import List
import math

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        seg_max_val = -1
        seg_min_val = math.inf
        last_seg_max_val = -1
        for i, num in enumerate(nums):
            if i == 0 or nums[i - 1].bit_count() == nums[i]:
                seg_max_val = max(seg_max_val, num)
                seg_min_val = min(seg_min_val, num)
                if seg_min_val < last_seg_max_val:
                    return False
            else:
                last_seg_max_val = seg_max_val
                seg_min_val = num
                seg_max_val = num
        return True


r = Solution().canSortArray([3,16,8,4,2])
print(r)