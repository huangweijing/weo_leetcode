class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)
        ans = str(n % 1000).rjust(3, "0")
        n //= 1000
        while n > 1000:
            ans = str(n % 1000).rjust(3, "0") + "." + ans
            n //= 1000
        if n == 0:
            return ans
        if n < 1000:
            return str(n % 1000) + "." + ans

r = Solution().thousandSeparator(55044094)
print(r)