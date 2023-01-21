class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ""
        while a > 0 or b > 0:
            if a == 0:
                ans += "b" * b
                b = 0
            elif b == 0:
                ans += "a" * a
                a = 0
            elif a > b:
                ans += "aab"
                a -= 2
                b -= 1
            elif b > a:
                ans += "bba"
                a -= 1
                b -= 2
            else:
                ans += "ab" * a
                a = 0
                b = 0
        return ans

r = Solution().strWithout3a3b(1, 2)
print(r)