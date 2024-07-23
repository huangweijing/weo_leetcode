class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        blank_bottles = 0
        while numBottles + blank_bottles >= numExchange:
            blank_bottles += numBottles
            ans += numBottles
            numBottles = 0
            while blank_bottles >= numExchange:
                blank_bottles -= numExchange
                numBottles += 1
                numExchange += 1
        ans += numBottles
        blank_bottles += numBottles
        numBottles = 0
        return ans