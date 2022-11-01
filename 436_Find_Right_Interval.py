from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        new_arr = list(zip(map(lambda x: x[0], intervals), range(len(intervals))))
        new_arr.sort(key=lambda x: x[0])
        start_arr, idx_arr = zip(* new_arr)
        ans = []
        for interval in intervals:
            idx = bisect.bisect_left(start_arr, interval[1])
            if idx == len(intervals):
                ans.append(-1)
            else:
                ans.append(idx_arr[idx])
        return ans

data = [[3,4],[2,3],[1,2]]
r = Solution().findRightInterval(data)
print(r)

