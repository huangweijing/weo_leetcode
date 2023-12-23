class Solution:
    def totalMoney(self, n: int) -> int:
        # weeks = n // 7
        # day = n % 7
        # return (28 + 28 + (weeks - 1) * 7) * weeks // 2 + \
        #        (weeks + 1 + weeks + day) * day // 2
        w, d = n // 7, n % 7
        return (49 * w + 7 * w ** 2 + 2 * w * d + d + d ** 2) >> 1

r = Solution().totalMoney(20)
print(r)

