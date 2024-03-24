from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr_cnt = Counter(arr)
        cnt_list = sorted([cnt for key, cnt in arr_cnt.items()], reverse=True)
        # print(cnt_list)
        while k > 0:
            if len(cnt_list) > 0 and cnt_list[-1] <= k:
                k -= cnt_list[-1]
                cnt_list.pop()
                # print(cnt_list)
            else:
                return len(cnt_list)
        return len(cnt_list)

data = [
    [5,5,4]
    , 1
]
r = Solution().findLeastNumOfUniqueInts(* data)
print(r)