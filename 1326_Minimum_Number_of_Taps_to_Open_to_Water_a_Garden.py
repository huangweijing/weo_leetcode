from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        range_arr = []
        for i, r in enumerate(ranges):
            range_arr.append([i - r, i + r])
        range_arr.sort(key=lambda x: x)
        covered_pt, idx = 0, 0
        ans = 0
        while covered_pt < n:
            okay_range = None
            while idx < len(range_arr) and range_arr[idx][0] <= covered_pt:
                if okay_range is None or okay_range[1] <= range_arr[idx][1]:
                    okay_range = range_arr[idx]
                idx += 1
            if okay_range is None:
                return -1
            covered_pt = okay_range[1]
            ans += 1
        return ans

data = [
    3
    , [0, 2, 0, 0]
]
r = Solution().minTaps(* data)
print(r)
