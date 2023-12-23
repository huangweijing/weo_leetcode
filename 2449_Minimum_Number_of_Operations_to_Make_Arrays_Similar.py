from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        num_even = [num for num in nums if num % 2 == 0]
        num_odd =  [num for num in nums if num % 2 == 1]
        target_even = [num for num in target if num % 2 == 0]
        target_odd =  [num for num in target if num % 2 == 1]
        num_even.sort()
        num_odd.sort()
        target_odd.sort()
        target_even.sort()
        ans = 0
        for i in range(len(num_even)):
            diff = target_even[i] - num_even[i]
            if diff > 0:
                ans += diff // 2
        for i in range(len(num_odd)):
            diff = target_odd[i] - num_odd[i]
            if diff > 0:
                ans += diff // 2
        return ans