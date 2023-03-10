class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for i in range(26):
            ch = chr(ord("a") + i)
