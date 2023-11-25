from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero_min_one = 0
        idx_dict = {0: -1}
        ans = 0
        for i, num in enumerate(nums):
            zero_min_one += 1 if num == 0 else -1
            if zero_min_one in idx_dict:
                ans = max(ans, i - idx_dict[zero_min_one])
            else:
                idx_dict[zero_min_one] = i
        return ans

data = [
    1,0,0,0,0,0,1,1
]
r = Solution().findMaxLength(data)
print(r)



