from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        # print(envelopes)
        idx = 0
        dp = SortedList()
        ans = 1
        while idx < len(envelopes):
            en = envelopes[idx]
            to_add = []
            while idx < len(envelopes) and en[0] == envelopes[idx][0]:
                inner = dp.bisect_left([envelopes[idx][1], 0]) - 1
                if inner == -1:
                    to_add.append([envelopes[idx][1], 1])
                    ans = max(ans, 1)
                else:
                    to_add.append([envelopes[idx][1], dp[inner][1] + 1])
                    ans = max(ans, dp[inner][1] + 1)
                idx += 1
            for ele in to_add:
                next_idx = dp.bisect_left(ele)
                # print("insert", ele, next_idx)
                while 0 <= next_idx < len(dp) and ele[1] >= dp[next_idx][1]:
                    dp.remove(dp[next_idx])
                    next_idx = dp.bisect_left(ele)
                dp.add(ele)
                # print(dp)

        return ans


data = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]
r = Solution().maxEnvelopes(data)
print(r)


