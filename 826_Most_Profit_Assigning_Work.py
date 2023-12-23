from typing import List
import bisect


class Solution:
    def maxProfitAssignment(self, difficulty: List[int]
                            , profit: List[int], worker: List[int]) -> int:
        diff_prof_arr = sorted(zip(difficulty, profit), key=lambda x: x[0])
        diff_arr = []
        max_prof_arr = []
        max_prof = 0
        for diff, prof in diff_prof_arr:
            diff_arr.append(diff)
            max_prof = max(max_prof, prof)
            max_prof_arr.append(max_prof)
        ans = 0
        for w in worker:
            idx = bisect.bisect_right(diff_arr, w) - 1
            if idx == -1:
                continue
            ans += max_prof_arr[idx]
        return ans


