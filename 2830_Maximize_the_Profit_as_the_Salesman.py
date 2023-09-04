from typing import List
import bisect


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: [x[1], x[0]])
        arr = []
        for offer in offers:
            if len(arr) == 0:
                arr.append([offer[1], offer[2]])
            else:
                # print(arr)
                idx = bisect.bisect_left(arr, [offer[0], -1])
                # print(arr, idx)
                if idx > 0:
                    idx -= 1
                    if arr[idx][1] + offer[2] > arr[-1][1]:
                        arr.append([offer[1], arr[idx][1] + offer[2]])
                else:
                    if offer[2] > arr[-1][1]:
                        arr.append([offer[1], offer[2]])
        return arr[-1][1]


data = [
    5
    , [[0,0,1],[0,2,10],[1,3,2]]
]
r = Solution().maximizeTheProfit(* data)
print(r)

# arr = [
#     [1, 2], [3, 7], [10, 10]
# ]
# i = bisect.bisect_left(arr, [3, 8], key=lambda x: x[1])
# print(i)
