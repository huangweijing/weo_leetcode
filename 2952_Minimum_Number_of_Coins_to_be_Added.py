from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        coins.append(target + 1)
        representable_cnt = 0
        ans = 0
        for coin in coins:
            while coin > representable_cnt + 1:
                ans += 1
                representable_cnt += representable_cnt + 1
            representable_cnt += coin

        return ans

data = [
    [15,1,12]
    , 43
    ]
# data = [
#     [1,1,1]
#     , 7
#     ]
r = Solution().minimumAddedCoins(*data)
print(r)