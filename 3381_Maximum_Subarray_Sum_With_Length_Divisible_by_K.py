from typing import List
import math


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -math.inf
        sum_arr = [0]
        for num in nums:
            sum_arr.append(sum_arr[-1] + num)
        for i in range(k):
            j = 1
            min_num = sum_arr[i]
            while i + k * j < len(sum_arr):
                ans = max(ans, sum_arr[i + k * j] - min_num)
                min_num = min(min_num, sum_arr[i + k * j])
                j += 1
        return ans


data = [
    [1,2]
    , 1
]
r = Solution().maxSubarraySum(*data)
print(r)