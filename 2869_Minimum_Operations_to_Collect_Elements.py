from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        my_set = set[int]()
        ans = 0
        while len(nums) > 0:
            ans += 1
            num = nums.pop()
            if 1 <= num <= k:
                my_set.add(num)
            if len(my_set) == k:
                return ans
        return -1
