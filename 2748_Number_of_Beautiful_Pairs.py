from functools import cache

class Solution:
    @cache
    def is_coprime(self, n1: int, n2: int):
        if n1 % 2 == 0 and n2 % 2 == 0:
            return False
        if n1 % 3 == 0 and n2 % 3 == 0:
            return False
        if n1 == n2 and n1 != 1:
            return False
        return True

    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                n1 = int(str(nums[i])[0])
                n2 = nums[j] % 10
                if self.is_coprime(n1, n2):
                    ans += 1
        return ans
