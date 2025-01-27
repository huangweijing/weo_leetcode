from typing import List
from collections import deque


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        idx_list = []
        for coin in coins:
            idx_list.append(coin[0])
            if coin[1] - k + 1>= 0:
                idx_list.append(coin[1] - k + 1)
        idx_list.sort()
        coins = deque(sorted(coins))
        ans = 0
        coin_bag = deque()
        full_bag_size = 0
        for idx in idx_list:
            end_idx = idx + k - 1
            while len(coin_bag) > 0 and coin_bag[0][1] < idx:
                coin = coin_bag.popleft()
                full_bag_size -= coin[2] * (coin[1] - coin[0] + 1)
            while len(coins) > 0 and coins[0][0] <= end_idx:
                coin = coins.popleft()
                coin_bag.append(coin)
                full_bag_size += coin[2] * (coin[1] - coin[0] + 1)
            bag_size = full_bag_size
            if len(coin_bag) > 0 and coin_bag[0][0] < idx:
                bag_size -= (idx - coin_bag[0][0]) * coin_bag[0][2]
            if len(coin_bag) > 0 and coin_bag[-1][1] > end_idx:
                bag_size -= (coin_bag[-1][1] - end_idx) * coin_bag[-1][2]
            ans = max(ans, bag_size)
            # print(idx, full_bag_size, bag_size, coin_bag)
        return ans
    

data = [
    [[1,10,3]]
    , 2
]
r = Solution().maximumCoins(*data)
print(r)
            