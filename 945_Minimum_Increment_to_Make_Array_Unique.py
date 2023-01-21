from typing import List
from collections import deque

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        nums = deque(nums)
        ans_arr = []
        while len(nums) > 0:
            num = nums.popleft()
            if len(ans_arr) == 0:
                ans_arr.append(num)
            elif len(ans_arr) > 0:
                top = ans_arr[-1]
                if num <= top:
                    ans_arr.append(top + 1)
                    ans += top + 1 - num
                else:
                    ans_arr.append(num)
        # print(ans_arr)
        return ans


r = Solution().minIncrementForUnique([1, 2, 2])
print(r)