class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s) >> 1):
            if s[i] != s[len(s) - i - 1]:
                ans += min(s[i], s[len(s) - i - 1])
            else:
                ans += s[i]
        if len(s) & 1 == 0:
            ans += ans[::-1]
        else:
            ans += (s[(len(s) >> 1)] + ans[::-1])
        return ans

r = Solution().makeSmallestPalindrome("egcfea")
print(r)
