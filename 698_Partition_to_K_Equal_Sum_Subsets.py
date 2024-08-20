from typing import List
from functools import cache

class Solution:

    def __init__(self) -> None:
        self.nums = []
        self.k = -1
        self.avg = -1

    @cache
    def my_sol(self, picked: int, remain:int) -> bool:
        if picked == (1 << (len(self.nums))) - 1:
            if remain == 0:
                return True
            else:
                return False
        if remain == 0:
            remain = self.avg
        for i, num in enumerate(self.nums):
            bit_picked = ((1 << i) & picked) >> i
            if bit_picked == 0 and num <= remain:
                res = self.my_sol(picked | ((1 << i)), remain - num)
                if res:
                    return True
        return False
        
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        self.nums, self.k = nums, k
        sum_nums = sum(nums)
        if sum_nums % k > 0:
            return False
        if max(nums) > sum_nums // k:
            return False
        self.avg = sum_nums // k
        return self.my_sol(0, 0)
    


data = [
    [815,625,3889,4471,60,494,944,1118,4623,497,771,679,1240,202,601,883]
    , 3
]
r = Solution().canPartitionKSubsets(*data)
print(r)