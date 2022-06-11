class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s) - 1
        len_last_word = 0
        while idx >= 0:
            if s[idx] == " ":
                if len_last_word > 0:
                    return len_last_word
                idx -= 1
                continue
            else:
                len_last_word += 1
            idx -= 1
        return len_last_word

sol = Solution()
l = sol.lengthOfLastWord("a")
print(l)

