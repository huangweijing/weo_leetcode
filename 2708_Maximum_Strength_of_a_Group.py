from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        ans, neg_min, pos_max = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            if num < 0:
                new_neg_min = min(num, num * pos_max, neg_min)
                new_pos_max = max(pos_max, num * neg_min)
            elif num > 0:
                new_neg_min = min(num * neg_min, neg_min)
                new_pos_max = max(num, num * pos_max, pos_max)
            else:
                new_neg_min = neg_min
                new_pos_max = pos_max
                ans = max(0, pos_max)
            ans = max(ans, new_pos_max)
            neg_min = new_neg_min
            pos_max = new_pos_max
        return ans

data = [-4]
r = Solution().maxStrength(data)
print(r)
