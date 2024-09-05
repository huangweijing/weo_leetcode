from typing import List
import math
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)
        for i in range(k):
            num = -heapq.heappop(nums)
            ans += num
            heapq.heappush(nums, -math.ceil(num / 3))
        return ans