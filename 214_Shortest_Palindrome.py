from collections import deque

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        pow = 26
        modolus = 10 ** 9 + 7
        hash1, hash2, base = 0, 0, 1
        max_equal_idx = 0
        for i in range(len(s)):
            ch_val = ord(s[i]) - ord("a") + 1
            hash1 = ((hash1 * pow) % modolus + ch_val) % modolus
            hash2 = (ch_val * base + hash2) % modolus
            base = (base * pow) % modolus
            if hash1 == hash2:
                max_equal_idx = i
        return s[max_equal_idx + 1:][::-1] + s

r = Solution().shortestPalindrome("a")
print(r)

