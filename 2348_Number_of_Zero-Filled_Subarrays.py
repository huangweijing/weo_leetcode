from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, i = 0, 0
        while i < len(nums):
            zero_cnt = 0
            while i < len(nums) and nums[i] == 0:
                zero_cnt += 1
                i += 1
            ans += (zero_cnt + 1) * zero_cnt // 2
            i += 1
        return ans

data = [0,0,0,2,0,0]
r = Solution().zeroFilledSubarray(data)
print(r)

