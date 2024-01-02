from typing import List
from collections import Counter


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int]
                              , numWanted: int, useLimit: int) -> int:
        lab_cnt = Counter()
        sort_list = sorted(zip(values, labels), key=lambda x: x[0], reverse=True)
        ans, num_cnt = 0, 0
        for val, lab in sort_list:
            if lab_cnt[lab] >= useLimit:
                continue
            ans += val
            lab_cnt[lab] += 1
            num_cnt += 1
            if num_cnt >= numWanted:
                break
        return ans


data = [
    [5,4,3,2,1]
    , [1,1,2,2,3]
    , 3
    , 1
]
r = Solution().largestValsFromLabels(* data)
print(r)