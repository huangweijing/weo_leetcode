class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        idx = 0
        last_ch = "0"
        ans = 0
        while idx < len(word):
            seq_len = 1
            while idx < len(word) and abs(ord(word[idx]) - ord(last_ch)) <= 1:
                seq_len += 1
                last_ch = word[idx]
                idx += 1
            ans += seq_len // 2
            if idx < len(word):
                last_ch = word[idx]
                idx += 1
        return ans
