from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for ch in str(num):
                ans.append(int(ch))
        return ans