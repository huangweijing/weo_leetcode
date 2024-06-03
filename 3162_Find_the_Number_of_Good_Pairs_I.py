from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for num in nums1:
            if num % k == 0:
                n = num // k
                for num2 in nums2:
                    if n % num2 == 0:
                        ans += 1
        return ans
