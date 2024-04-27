class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zero, one = 0, 0
        max_zero, max_one = 0, 0
        for ch in s:
            if ch == "0":
                one = 0
                zero += 1
            else:
                one += 1
                zero = 0
            max_zero = max(max_zero, zero)
            max_one = max(max_one, one)
        return max_one > max_zero


