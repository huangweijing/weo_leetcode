class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        ans = 0
        for i in reversed(range(len(s))):
            if s[i] == " ":
                break
            ans += 1
        return ans


sol = Solution()
l = sol.lengthOfLastWord("a 92134")
print(l)


