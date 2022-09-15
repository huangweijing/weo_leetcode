class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n > 0:
            dig = n % k
            result += dig
            n = int(n / k)
        return result
