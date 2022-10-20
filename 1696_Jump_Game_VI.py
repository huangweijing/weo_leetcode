import math
from typing import List
from functools import cache
from collections import deque

class Solution:
    def __init__(self):
        self.nums = []
        self.k = 0

    @cache
    def my_sol(self, idx) -> int:
        if idx == 0:
            return self.nums[0]
        ans = -math.inf
        need_check = deque()
        for i in range(1, min(self.k, idx) + 1):
            if self.nums[idx - i] > 0:
                return self.nums[idx] + self.my_sol(idx - i)
            else:
                while len(need_check) > 0 and need_check[-1][1] <= self.nums[idx - i]:
                    need_check.pop()
                need_check.append([i, self.nums[idx - i]])
        # print(self.nums, idx, need_check)
        for i, _ in need_check:
            ans = max(ans, self.nums[idx] + self.my_sol(idx - i))

        return ans

    def maxResult(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        for i in range(0, len(nums), 1500):
            self.my_sol(i)
        return self.my_sol(len(nums) - 1)

data = [[-8,-7,-6,-5,-4,-3,-2,-1]
, 4]
import sys
sys.setrecursionlimit(1500)
r = Solution().maxResult(*data)
print(r)


# import heapq
# from collections import deque
# h = deque([7, 2, 9, 4, 8])
# heapq.heapify(h)
# print(heapq.heappop())

