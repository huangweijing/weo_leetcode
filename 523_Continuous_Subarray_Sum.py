from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_dict = { 0: -1 }
        sum_mod= 0
        for i, num in enumerate(nums):
            sum_mod = (sum_mod + num) % k
            if sum_mod % k in mod_dict:
                if i - mod_dict[sum_mod] > 1:
                    return True
            else:
                mod_dict[sum_mod] = i
            # print(mod_dict)
        return False

data = [
    [5, 0, 0, 0]
    , 3
]
r = Solution().checkSubarraySum(* data)
print(r)