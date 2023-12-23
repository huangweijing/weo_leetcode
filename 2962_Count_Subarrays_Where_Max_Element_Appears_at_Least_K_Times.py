from typing import List
from collections import Counter


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        max_arr = [i for i in range(len(nums)) if nums[i] == max_num]
        ans = 0
        last_idx = -1
        # print(max_arr, len(nums))
        for i in range(len(max_arr)):
            pre_len = max_arr[i] - last_idx
            if i + k - 1 >= len(max_arr):
                break
            suf_len = len(nums) - max_arr[i + k - 1]
            last_idx = max_arr[i]
            # print(pre_len, suf_len)
            ans += pre_len * suf_len
        return ans



data = [
    [1,3,3,5,2,4,5,3,2,3,5,5,3]
    # [1,3,2,3,3]
    , 2
]
r = Solution().countSubarrays(*data)
print(r)