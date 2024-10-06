class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if target.find("1") != -1 and s.find("1") != -1:
            return True
        return s == target
            