from typing import List
from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod60 = Counter()
        for dur in time:
            mod60[dur % 60] += 1
        # print(mod60)
        ans = 0
        for i in range(31):
            if i == 0:
                if mod60[i] > 1:
                    ans += mod60[i] * (mod60[i] - 1) // 2
                # elif mod60[i] == 1:
                #     ans += 1
            elif i == 30:
                ans += mod60[i] * (mod60[i] - 1) // 2
            else:
                ans += mod60[i] * mod60[60 - i]
            # print(i, ans)
        return ans


    # [30,20,150,100,40]
    # , [60,60,60]
    # , [60,60,30,30,30]
    # , [60,60,30]
    # , [10,20,30]
data = [418,204,77,278,239,457,284,263,372,279,476,416,360,18]
r = Solution().numPairsDivisibleBy60(data)
print(r)

