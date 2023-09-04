def shift(ch: str, i: int) -> str:
    return chr(ord(ch) + i)

class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        i = 0
        while i * 2 < len(s):
            ans += s[i * 2]
            if i * 2 + 1 < len(s):
                ans += shift(s[i * 2], int(s[i * 2 + 1]))
            i += 1
        return ans

r = Solution().replaceDigits("a1b2c3d4e")
print(r)