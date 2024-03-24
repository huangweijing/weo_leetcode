class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty_bottles = 0
        while numBottles > 0:
            ans += numBottles
            empty_bottles += numBottles
            numBottles = empty_bottles // numExchange
            empty_bottles %= numExchange
        return ans

