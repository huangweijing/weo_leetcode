from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        cnt = cnt_s & cnt_t
        cnt = cnt_s - cnt
        return sum(cnt.values())

r = Solution().minSteps("aabb", "bbab")
print(r)

