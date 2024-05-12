class Solution:
    def generateTheString(self, n: int) -> str:
        if n & 1 == 1:
            return "a" * n
        else:
            return "a" + "b" * (n - 1)
