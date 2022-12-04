from typing import List

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        # for i in range(len(nums)):
        non_increasing_len_arr = []
        for i, num in enumerate(nums):
            if len(non_increasing_len_arr) > 0 and nums[i] <= nums[i - 1]:
                non_increasing_len_arr.append(non_increasing_len_arr[-1] + 1)
            else:
                non_increasing_len_arr.append(1)
        # print(non_increasing_len_arr)

        non_decreasing_len_arr = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1 and nums[i] <= nums[i + 1]:
                non_decreasing_len_arr[i] = non_decreasing_len_arr[i + 1] + 1
            else:
                non_decreasing_len_arr[i] = 1
        # print(non_decreasing_len_arr)

        ans = []
        for i in range(k, len(nums) - k):
            if non_increasing_len_arr[i - 1] >= k and non_decreasing_len_arr[i + 1] >= k:
                ans.append(i)
        return ans

data = [
    [440043,276285,336957]
    , 1
]
r = Solution().goodIndices(* data)
print(r)

