from collections import Counter


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = Counter(s)
        total_cnt = cnt["a"] + cnt["e"] + cnt["i"] + cnt["o"] + cnt["u"]
        return total_cnt > 0


r = Solution().doesAliceWin("abc")
print(r)
