from typing import List

class Solution:
    def find_pos(self, intervals: list[list[int]], num: int):
        left_wall = 0
        right_wall = len(intervals)
        idx = (left_wall + right_wall) >> 1
        while left_wall < right_wall:
            if intervals[idx][0] == num:
                return idx
            elif intervals[idx][0] < num:
                if idx == len(intervals) - 1:
                    return len(intervals)
                elif intervals[idx][0] < num < intervals[idx + 1][0]:
                    return idx + 1
                left_wall = idx
            else:
                if idx == 0:
                    return -1
                right_wall = idx

            idx = (left_wall + right_wall) >> 1
        return idx

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        pos = self.find_pos(intervals, newInterval[0])
        if pos > 0:
            if intervals[pos - 1][1] >= newInterval[0]:
                newInterval[0] = intervals[pos - 1][0]
                pos -= 1
        if pos == -1:
            idx = 0
            while idx < len(intervals) and newInterval[1] >= intervals[idx][0]:
                newInterval[1] = max(newInterval[1], intervals[idx][1])
                idx += 1
            # print(f"idx={idx}, len(intervals)={len(intervals)}")
            result.append(newInterval)
            if idx < len(intervals):
                result.extend(intervals[idx:])
        elif pos == len(intervals):
            result.extend(intervals)
            result.append(newInterval)
        else:
            idx = pos
            while idx < len(intervals) and newInterval[1] >= intervals[idx][0]:
                idx += 1
            newInterval[1] = max(newInterval[1], intervals[idx - 1][1])
            result.extend(intervals[:pos])
            result.append(newInterval)
            if idx < len(intervals):
                result.extend(intervals[idx:])

        return result

r = Solution().insert([], [4, 8])
print(r)
