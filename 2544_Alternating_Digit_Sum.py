class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num_str = str(n)
        ans = 0
        sign = 1
        for dig in num_str:
            int_dig = ord(dig) - ord("0")
            ans += int_dig * sign
            sign *= -1
        return ans

r = Solution().alternateDigitSum(111)
print(r)

