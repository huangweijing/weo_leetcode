class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s) > 1:
            s = str(sum(map(int, s)))
        return int(s)

