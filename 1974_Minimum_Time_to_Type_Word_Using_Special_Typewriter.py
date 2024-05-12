class Solution:
    def minTimeToType(self, word: str) -> int:
        last_pos = "a"
        ans = 0
        for ch in word:
            ans += min(abs(ord(ch) - ord(last_pos) + 26) % 26
                , abs(ord(last_pos) - ord(ch) + 26) % 26)
            ans += 1
            last_pos = ch
        return ans
