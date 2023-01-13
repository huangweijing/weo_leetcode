from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        if cnt["a"] < k or cnt["b"] < k or cnt["c"] < k:
            return -1
        left, right = len(s), 0
        ans = left + right
        while left > 0:
            left_ch = s[left - 1]
            cnt[left_ch] -= 1
            left -= 1
            while cnt[left_ch] < k:
                right += 1
                right_ch = s[-right]
                cnt[right_ch] += 1
            ans = min(ans, left + right)
        return ans

data = [
    "a"
    , 2
]
r = Solution().takeCharacters(* data)
print(r)

