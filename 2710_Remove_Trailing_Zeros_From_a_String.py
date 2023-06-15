class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        not_zero_idx = len(num) - 1
        while num[not_zero_idx] == "0":
            not_zero_idx -= 1
        return num[:not_zero_idx + 1]