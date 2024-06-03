class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel_cnt, consonant_cnt = 0, 0
        for ch in word:
            if not ("0" <= ch <= "9" or "a" <= ch <= "z" or "A" <= ch <= "Z"):
                return False
            if vowel_cnt == 0 and ch.lower() in ("a", "i", "u", "e", "o"):
                vowel_cnt += 1
            if consonant_cnt == 0 and "a" <= ch.lower() <= "z" and ch.lower() not in ("a", "i", "u", "e", "o"):
                consonant_cnt += 1
        if vowel_cnt == 0 or consonant_cnt == 0:
            return False
        return True


r = Solution().isValid("xiUz")
print(r)