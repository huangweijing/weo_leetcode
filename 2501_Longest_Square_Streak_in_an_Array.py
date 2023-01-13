from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_arr = [0] * (10 ** 5 + 1)
        sqrt_max = int((10 ** 5 + 1) ** 0.5) + 1
        max_num = 0
        for num in nums:
            num_arr[num] = 1
            max_num = max(max_num, num)
        ans = -1
        for i, num in enumerate(num_arr):
            if i > max_num:
                break
            if num == 0:
                continue
            else:
               ans = max(ans, num)
               if i >= sqrt_max:
                   continue
               if num_arr[i ** 2] != 0:
                   num_arr[i ** 2] = max(num_arr[i ** 2], num + 1)
        return -1 if ans == 1 else ans

data = [
    [2,3,5,6,7]
]
r = Solution().longestSquareStreak(* data)
print(r)

