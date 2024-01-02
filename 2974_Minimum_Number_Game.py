from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        ans = []
        while len(nums) > 0:
            ali = nums.pop()
            bob = nums.pop()
            ans.append(bob)
            ans.append(ali)
        return ans

