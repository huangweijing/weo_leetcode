from typing import List
from collections import Counter


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff_dict_arr = [Counter() for _ in nums]
        end_diff_dict_arr = [Counter() for _ in nums]
        ans = 0
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                diff_dict_arr[j][diff] = diff_dict_arr[j][diff] + 1
                end_diff_dict_arr[j][diff] += end_diff_dict_arr[i][diff] + diff_dict_arr[i][diff]
        for item in end_diff_dict_arr:
            ans += sum(item.values())
        return ans

data = [2,4,6,8,10]
r = Solution().numberOfArithmeticSlices(data)
print(r)

