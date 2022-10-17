from typing import List
import math
import heapq

class MaximumHeap:
    def __init__(self):
        self.data = []
        heapq.heapify(self.data)

    def top(self):
        if len(self.data) == 0:
            return None
        return -self.data[0]

    def pop(self) -> int:
        return -heapq.heappop(self.data)

    def push(self, num: int):
        heapq.heappush(self.data, -num)

    def length(self) -> int:
        return len(self.data)


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: x[0])
        idx, cnt, max_end = 0, 0, 0
        h = MaximumHeap()
        while idx < len(clips):
            while idx < len(clips):
                if clips[idx][0] <= max_end:
                    h.push(clips[idx][1])
                else:
                    break
                idx += 1
            if h.length() == 0:
                return -1
            max_end = h.pop()
            cnt += 1
            if max_end >= time:
                break
        if max_end >= time:
            return cnt
        else:
            return -1

data = [[[0,2],[4,8]]
,5]
r = Solution().videoStitching(*data)
print(r)