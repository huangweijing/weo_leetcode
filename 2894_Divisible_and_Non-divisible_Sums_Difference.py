class Solution:
    @classmethod
    def get_sum(cls, num: int, from_num: int = 1) -> int:
        return (from_num + num) * (num - from_num + 1) // 2

    def differenceOfSums(self, n: int, m: int) -> int:
        return Solution.get_sum(n) - 2 * m * Solution.get_sum(n // m)


r = Solution().differenceOfSums(10, 3)
print(r)