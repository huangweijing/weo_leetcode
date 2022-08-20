import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        p = re.compile("^([A-Z]+|[a-z]+|[A-Z][a-z]*)$")
        return p.match(word) is not None

r = Solution().detectCapitalUse("AAA")
print(r)

