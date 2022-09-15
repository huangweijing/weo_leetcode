from typing import List

class Solution:
    def get_gcd(self, n1: int, n2: int) -> int:
        gcd = min(n1, n2)
        while gcd >= 1:
            if n1 % gcd == 0 and n2 % gcd == 0:
                return gcd
            gcd -= 1

    def findGCD(self, nums: List[int]) -> int:
        return self.get_gcd(min(nums), max(nums))
