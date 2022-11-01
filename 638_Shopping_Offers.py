from typing import List
import math

class Solution:
    BASE = 11

    def __init__(self):
        self.price = []
        self.special = []
        self.dp = dict[int, int]()

    def hash_need(self, needs: list[int]):
        hash_key = 0
        for need in needs:
            hash_key = hash_key * Solution.BASE + need
        return hash_key

    def is_available(self, needs: list[int], special_offer: list[int]) -> bool:
        for i, need in enumerate(needs):
            if need < special_offer[i]:
                return False
        return True

    def get_available_offer(self, needs: list[int]) -> list[list[int]]:
        return [offer for offer in self.special if self.is_available(needs, offer)]

    def use_offer(self, needs: list[int], offer: list[int]) -> list[int]:
        needs_after = needs.copy()
        for i in range(len(needs_after)):
            needs_after[i] -= offer[i]
        return needs_after

    def just_buy_them(self, needs: list[int]) -> int:
        return sum(map(lambda x: x[0] * x[1], zip(needs, self.price)))

    def my_min_offers(self, needs: list[int]) -> int:
        hash_key = self.hash_need(needs)
        if hash_key in self.dp:
            return self.dp[hash_key]
        ans = self.just_buy_them(needs)
        offers = self.get_available_offer(needs)
        # print(offers)
        for offer in offers:
            needs_used_offer = self.use_offer(needs, offer)
            cost = self.my_min_offers(needs_used_offer) + offer[-1]
            ans = min(ans, cost)

        self.dp[hash_key] = ans
        return ans

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.price, self.special = price, special
        return self.my_min_offers(needs)

data = [
    [2, 3, 4]
    , [[1, 1, 0, 4], [2, 2, 1, 9]]
    , [1, 2, 1]
]
r = Solution().shoppingOffers(*data)
print(r)
