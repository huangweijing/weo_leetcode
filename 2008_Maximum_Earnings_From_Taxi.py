from typing import List
import bisect


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: [x[1], x[0]])
        # print(rides)
        dp = []
        idx = 0
        while idx < len(rides):
            ride0 = rides[idx]
            to_append = 0
            # print("processing", ride0[1])
            while idx < len(rides) and rides[idx][1] == ride0[1]:
                ride = rides[idx]
                find = bisect.bisect_left(dp, [ride[0] + 1, -1]) - 1
                rev = ride[1] - ride[0] + ride[2]
                # print(find, dp)
                if find == -1:
                    if rev > to_append:
                        to_append = rev
                else:
                    if dp[find][1] + rev > to_append:
                        to_append = dp[find][1] + rev
                idx += 1
            if len(dp) == 0 or to_append > dp[-1][1]:
                dp.append([ride[1], to_append])
            # print(dp)
        return dp[-1][1]
    

data = [
    10
    , [[9,10,2],[4,5,6],[6,8,1],[1,5,5],[4,9,5],[1,6,5],[4,8,3],[4,7,10],[1,9,8],[2,3,5]]
]
r = Solution().maxTaxiEarnings(*data)
print(r)