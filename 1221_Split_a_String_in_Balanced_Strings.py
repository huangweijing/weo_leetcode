from collections import Counter

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = Counter()
        ans = 0
        for ch in s:
            cnt[ch] += 1
            if cnt["L"] == cnt["R"]:
                cnt = Counter()
                ans += 1
        return ans
