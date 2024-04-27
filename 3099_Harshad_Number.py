class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum(map(int, str(x)))
        if x % s == 0:
            return s
        return -1