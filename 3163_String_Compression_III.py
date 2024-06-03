class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        idx = 0
        while idx < len(word):
            ch_cnt = 0
            ch = word[idx]
            while idx < len(word) and word[idx] == ch and ch_cnt < 9:
                ch_cnt += 1
                idx += 1
            ans += str(ch_cnt) + ch
        return ans


data = "aaaaaaaaaabbbc"
r = Solution().compressedString(data)
print(r)
