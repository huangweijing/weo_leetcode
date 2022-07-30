class Solution:
    def trailingZeroes(self, n: int) -> int:
        lucky_five = 0
        for i in range(n + 1):
            cur = i
            while cur % 5 == 0 and cur > 0:
                lucky_five += 1
                cur = cur / 5
                # print(cur)
        return lucky_five

r = Solution().trailingZeroes(10000)
print(r)
