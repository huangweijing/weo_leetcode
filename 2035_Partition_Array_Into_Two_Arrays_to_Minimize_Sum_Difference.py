from typing import List
from collections import defaultdict
import math


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: list[int]())
        sum_all = sum(nums)
        nums.sort()
        # print(sum_all, nums)
        max_key = 0
        for num in nums:
            for key in reversed(range(len(dp), 0, -1)):
                if key >= len(nums) // 2:
                    continue
                for val in dp[key]:
                    # if val + num <= sum_all // 2:
                    dp[key + 1].append(val + num)
            # if num <= sum_all // 2:
            dp[1].append(num)
            print(dp)
        ans = math.inf
        for val in dp[len(nums) // 2]:
            ans = min(ans, abs(sum_all - val * 2))
        return ans


# data = [-36, 36]
data = [7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]
r = Solution().minimumDifference(data)
print(r)