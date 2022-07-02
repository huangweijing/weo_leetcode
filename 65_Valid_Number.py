import re

class Solution:
    def isNumber(self, s: str) -> bool:
        integer = "[+-]?\d+"
        decimal = "([+-]?\d+\.\d+)|([+-]?\d+\.)|([+-]?\.\d+)"
        number = f"^({decimal}|{integer})([eE]{integer})?$"
        return re.search(number, s) is not None

sol = Solution()
r = sol.isNumber("-.1E-123")
print(r)