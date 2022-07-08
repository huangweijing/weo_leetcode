class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        n = 0
        while left != right:
            left >>= 1
            right >>= 1
            n += 1

        while n > 0:
            left <<= 1
            n -= 1

        return left

r = Solution().rangeBitwiseAnd(10, 15)
print(r)
