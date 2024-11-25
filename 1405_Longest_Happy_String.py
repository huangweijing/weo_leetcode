class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = list(sorted([[a, "a"], [b, "b"], [c, "c"]]))
        ans = ""
        while chars[-1][0] > 0:
            if len(ans) == 0 or ans[-1] != chars[-1][1]:
                ans += min(chars[-1][0], 2) * chars[-1][1]
                chars[-1][0] -= min(chars[-1][0], 2)
            else:
                if chars[-2][0] == 0:
                    break
                else:
                    ans += chars[-2][1]
                    chars[-2][0] -= 1
            chars.sort()
        return ans
            
data = [
    1
    , 12
    , 7
]
r = Solution().longestDiverseString(*data)
print(r)