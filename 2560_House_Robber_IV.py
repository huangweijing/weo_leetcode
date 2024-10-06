from typing import List


class Solution:
    def __init__(self) -> None:
        self.nums = []
        self.k = -1

    def my_sol(self, capacity: int) -> bool:
        idx = 0
        cnt = self.k
        while idx < len(self.nums):
            if self.nums[idx] <= capacity:
                cnt -= 1
                idx += 2
            else:
                idx += 1
            if cnt == 0:
                return True
        return False
            

    def minCapability(self, nums: List[int], k: int) -> int:
        self.nums, self.k = nums, k
        left, right = 0, 1000000001
        mid = (left + right) >> 1
        while left <= right:
            s1 = self.my_sol(mid)
            s2 = self.my_sol(mid - 1)
            if s1 and not s2:
                return mid
            elif s2 and s1:
                right = mid - 1
            elif not s1 and not s2:
                left = mid + 1
            mid = (left + right) >> 1
        return mid
    

data = [
    [2,7,9,3,1]
    , 2
]
r = Solution().minCapability(* data)
print(r)