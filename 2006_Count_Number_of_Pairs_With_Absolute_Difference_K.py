from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        arr = [0] * 101
        for num in nums:
            arr[num] += 1
        ans = 0
        for i in range(101):
            if i + k > 100:
                break
            ans += arr[i] * arr[i + k]
        return ans
