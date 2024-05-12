from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            is_pali = True
            for i in range(len(word) // 2):
                if not word[len(word) - 1 - i] == word[i]:
                    is_pali = False
                    break
            if is_pali:
                return word
        return ""
