class Solution:
    def smallestString(self, s: str) -> str:
        skipping = True
        ans = ""
        for i, ch in enumerate(s):
            if skipping and ch == "a":
                ans += ch
                continue
            else:
                skipping = False
                if ch == "a":
                    ans += s[i:]
                    break
                else:
                    ans += chr(ord(ch) - 1)
        if skipping:
            return ans[:-1] + "z"
        else:
            return ans


r = Solution().smallestString("aaaaaa")
print(r)

