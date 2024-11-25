from typing import List
import bisect


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        item_list = []
        for item in items:
            if len(item_list) == 0 or item[1] > item_list[-1][1]:
                item_list.append(item)
        ans = []
        for query in queries:
            idx = bisect.bisect_left(item_list, [query, 10e9]) - 1
            if idx == -1:
                ans.append(0)
            else:
                ans.append(item_list[idx][1])
        return ans
    

data = [
    [[1,2],[3,2],[2,4],[5,6],[3,5]]
    , [1,2,3,4,5,6]
]
r = Solution().maximumBeauty(*data)
print(r)

        