class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        drt = (time // (n - 1)) % 2
        pos = time % (n - 1)
        if drt == 0:
            return pos + 1
        else:
            return n - pos