class Solution:
    def freqAlphabets(self, s: str) -> str:
        code_dic = { str(i) + ("#" if i > 9 else "") : chr(i - 1 + ord("a"))
                     for i in range(1, 27) }
        idx = 0
        ans = ""
        while idx < len(s):
            code = s[idx: idx + 3]
            if code in code_dic:
                ans += code_dic[code]
                idx += 3
            else:
                ans += code_dic[s[idx: idx + 1]]
                idx += 1
        return ans

data = "10#11#12"
r = Solution().freqAlphabets(data)
print(r)