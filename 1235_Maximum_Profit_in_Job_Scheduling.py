from typing import List
from sortedcontainers import SortedList
import math


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        # print(list(jobs))
        sl = SortedList(key=lambda x: [x[0], x[1]])
        for job in jobs:
            idx = sl.bisect_left([job[0], math.inf]) - 1
            if idx == -1:
                end_time_idx = sl.bisect_left([job[1], 0])
                while end_time_idx < len(sl) and sl[end_time_idx][1] <= job[2]:
                    sl.pop(end_time_idx)
                if end_time_idx == 0 or sl[end_time_idx - 1][1] < job[2]:
                    sl.add([job[1], job[2]])
            else:
                new_job = [job[1], sl[idx][1] + job[2]]
                # print(f"find new job {new_job}")
                end_time_idx = sl.bisect_left([new_job[0], 0])
                while end_time_idx < len(sl) and sl[end_time_idx][1] <= new_job[1]:
                    sl.pop(end_time_idx)
                if end_time_idx == 0 or sl[end_time_idx - 1][1] < new_job[1]:
                    sl.add([new_job[0], new_job[1]])
            # print(sl)
        return max(x[1] for x in sl)


data = [
[33,8,9,18,16,36,18,4,42,45,29,43]
, [40,16,32,39,46,43,28,13,44,46,39,44]
, [2,6,5,14,5,19,5,12,19,14,14,17]
]
r = Solution().jobScheduling(*data)
print(r)


