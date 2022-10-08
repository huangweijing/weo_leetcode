class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            idx = s.find(part)
            if idx == -1:
                break
            s = s[:idx] + s[idx + len(part):]
        return s

r = Solution().removeOccurrences("aabababa", "aba")
print(r)
# print(r.find("abc"))