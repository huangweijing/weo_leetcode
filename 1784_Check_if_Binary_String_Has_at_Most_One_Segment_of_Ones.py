class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        idx = 0
        while idx < len(s) and s[idx] == "0":
            idx += 1
        while idx < len(s) and s[idx] == "1":
            idx += 1
        while idx < len(s):
            if s[idx] == "1":
                return False
            idx += 1
        return True