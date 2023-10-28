from functools import cache


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        pre_val = self.kthGrammar(n - 1, (k + 1) >> 1)
        return 1 - pre_val ^ (k & 1)


r = Solution().kthGrammar(4, 6)
print(r)

