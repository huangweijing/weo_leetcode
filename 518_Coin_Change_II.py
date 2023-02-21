from typing import List
from functools import cache


class Solution:
    def __init__(self):
        self.coins = []

    @cache
    def my_sol(self, amount: int, available_coin_len: int):
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        ans = 0
        for i in range(0, available_coin_len):
            coin = self.coins[i]
            ans += self.my_sol(amount - coin, i + 1)
            # print(f"coin={coin}, amount={amount}"
            #       f", available_coin_len={available_coin_len}, ans={ans}")

        return ans

    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = coins
        return self.my_sol(amount, len(coins))


data = [
    5,
    [1, 2, 5]
]
r = Solution().change(* data)
print(r)
