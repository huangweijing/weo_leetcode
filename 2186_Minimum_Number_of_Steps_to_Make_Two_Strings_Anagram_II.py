from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scnt, tcnt = Counter(s), Counter(t)
        return sum((scnt - tcnt).values()) + sum((tcnt - scnt).values())

data = [
    "leetcode"
    , "coats"
]
r = Solution().minSteps(* data)
print(r)
