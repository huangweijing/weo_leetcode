from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mod_all = sum(nums) % p
        if mod_all == 0:
            return 0
        pre_sum = 0
        mod_p = dict[int, int]()
        ans = len(nums)
        for i, num in enumerate(nums):
            pre_sum += num
            to_find = (pre_sum % p + p - mod_all) % p
            if to_find == 0:
                ans = min(ans, i + 1)
            if to_find in mod_p:
                ans = min(ans, i - mod_p[to_find])
            mod_p[pre_sum % p] = i
        if ans == len(nums):
            return -1
        return ans
    

data = [
    [2,2,2,2,2]
    , 6
]
r = Solution().minSubarray(*data)
print(r)
                
            
