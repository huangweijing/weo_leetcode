from typing import List
from collections import defaultdict

class Solution:
    def relocateMarbles(self, nums: List[int]
                        , moveFrom: List[int], moveTo: List[int]) -> List[int]:
        num_set = set(nums)
        for i in range(len(moveTo)):
            if moveFrom[i] in num_set:
                num_set.remove(moveFrom[i])
                num_set.add(moveTo[i])
        ans = list(num_set)
        ans.sort()
        return ans


        # move_tbl = dict[int, int]()
        # src_tbl = defaultdict(lambda : set[int]())
        # for i in range(len(moveTo)):
        #     move_tbl[moveFrom[i]] = moveTo[i]
        #     src_tbl[moveTo[i]].add(moveFrom[i])
        #     if moveFrom[i] in src_tbl:
        #         change_list = src_tbl[moveFrom[i]]
        #         for item in change_list:
        #             move_tbl[item] = moveTo[i]
        #         del src_tbl[moveFrom[i]]
        #         change_list.add(moveFrom[i])
        #         src_tbl[moveTo[i]] = change_list
        #     print(moveFrom[i], moveTo[i])
        #     print(move_tbl)
        #     print(src_tbl)
        #     print()
        #
        #
        # ans = set[int]()
        # for num in nums:
        #     if num in move_tbl:
        #         ans.add(move_tbl[num])
        #     else:
        #         ans.add(num)
        # ans = list(ans)
        # ans.sort()
        # return ans

data = [
    [2, 45, 45, 48, 51, 57, 67, 73, 78, 78]
    , [78, 67, 45, 34, 51, 62, 48, 95, 2, 67]
    , [34, 65, 62, 95, 62, 12, 85, 67, 79, 71]
]
# [12,57,71,73,79,85]
# [12,57,65,71,73,79,85]
r = Solution().relocateMarbles(* data)
print(r)