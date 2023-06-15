class Solution:
    def minLength(self, s: str) -> int:
        old_len = len(s)
        new_len = 0
        while old_len != new_len:
            old_len = len(s)
            s = s.replace("AB", "")
            s = s.replace("CD", "")
            new_len = len(s)
        return len(s)