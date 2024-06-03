from typing import List
import bisect


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        last = nums[0]
        problem_arr = []
        for i, num in enumerate(nums[1:], start=1):
            if num & 1 == last & 1:
                problem_arr.append(i)
            last = num
        # print(problem_arr)
        ans = []
        for query in queries:
            idx1 = bisect.bisect_right(problem_arr, query[0]) - 1
            idx2 = bisect.bisect_right(problem_arr, query[1]) - 1
            # print(idx1, idx2)
            if idx1 == idx2:
                ans.append(True)
            else:
                ans.append(False)
        return ans


data = [
    [1,3,2]
    , [[0,1]]
]
r = Solution().isArraySpecial(* data)
print(r)