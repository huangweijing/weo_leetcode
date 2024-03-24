from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return len([1 for i, s in enumerate(startTime) if s <= queryTime <= endTime[i]])

