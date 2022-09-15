class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if ord(num[i]) - ord("0") & 1 == 1:
                return num[:i + 1]
        return ""
