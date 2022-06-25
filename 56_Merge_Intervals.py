from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        result = list[list[int]]()
        idx = 0
        while idx < len(intervals):
            nump = intervals[idx].copy()
            if idx + 1 < len(intervals):
                if nump[1] < intervals[idx + 1][0]:
                    result.append(nump)
                else:
                    new_idx = idx + 1
                    while new_idx < len(intervals) and nump[1] >= intervals[new_idx][0]:
                        nump[1] = max(intervals[new_idx][1], nump[1])
                        new_idx += 1
                    result.append(nump)
                    idx = new_idx
                    continue
            else:
                result.append(nump)

            idx += 1
        return result

r = Solution().merge([[1,4],[4,5]])
print(r)