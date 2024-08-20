class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(list(s)))
        ans = s
        for i in range(len(s)):
            ans = min(ans, s[i: ] + s[: i])
        return ans
    
r = Solution().orderlyQueue("cba", 1)
print(r)