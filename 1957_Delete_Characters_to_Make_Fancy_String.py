class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        ans = ""
        while i < len(s):
            ch = s[i]
            cnt = 0
            while i < len(s) and s[i] == ch:
                cnt += 1
                i += 1
            if cnt >= 3:
                ans += ch * 2
            else:
                ans += ch * cnt
        return ans


data = "bbbaacdddddddcc"
r = Solution().makeFancyString(data)
print(r)
