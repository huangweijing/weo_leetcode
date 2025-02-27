from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        op_cnt = 0
        while len(nums) >= 2:
            n1 = heapq.heappop(nums)
            if n1 >= k:
                break
            n2 = heapq.heappop(nums)
            heapq.heappush(nums, n1 * 2 + n2)
            op_cnt += 1
        return op_cnt

data = [
    [1,1,2,4,9]
    , 20
]
r = Solution().minOperations(*data)
print(r)