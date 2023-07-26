from typing import List

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        diff_arr = [0] * len(nums)
        diff_len_arr = [1] * len(nums)
        ans = 0
        found = False
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff == 1:
                found = True
                if diff_arr[i - 1] == -diff:
                    diff_len_arr[i] = diff_len_arr[i - 1] + 1
                else:
                    diff_len_arr[i] = 2
            elif diff == -1:
                if diff_arr[i - 1] == -diff:
                    diff_len_arr[i] = diff_len_arr[i - 1] + 1

            diff_arr[i] = diff
            ans = max(ans, diff_len_arr[i])
        # print(diff_arr)
        # print(diff_len_arr)
        if not found:
            return -1
        return ans

# r = Solution().alternatingSubarray([14,30,29,49,3,23,44,21,26,52])

r = Solution().alternatingSubarray([2,3,4,3,4])
print(r)



