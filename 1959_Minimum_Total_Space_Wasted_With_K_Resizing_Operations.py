from typing import List
from collections import Counter, deque


class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        dp = [Counter()]
        bigger_arr = deque()
        stack = []
        for num in reversed(nums):
            while len(stack) > 0 and stack[-1] <= num:
                stack.pop()
            stack.append(num)
            bigger_arr.appendleft(stack.copy())
            # print(stack)
        for bigger in bigger_arr[0]:
            dp[0][bigger] = 0
        print(bigger_arr)
            
        print(dp)
        for j, num in enumerate(nums):
            new_dp = [Counter() for _ in dp]
            for i, dp_entry in enumerate(dp):
                for size, cost in dp_entry.items():
                    if size >= num:
                        new_dp[i][size] = cost + size - num
                if i + 1 <= k:
                    min_val = min(dp_entry.values())
                    # print(min_val)
                    if i + 1 == len(new_dp):
                        new_dp.append(Counter())
                    for bigger in bigger_arr[j]:
                        new_dp[i + 1][bigger] = min_val + bigger - num
            dp = new_dp
            print(num, dp)

        ans = 10e9
        for dp_entry in dp:
            print(dp_entry)
            ans = min(ans, min(dp_entry.values()))
        return ans
    

data = [
    [10,14,49,22,7,6,25]
    , 2
]
r = Solution().minSpaceWastedKResizing(*data)
print(r)
                