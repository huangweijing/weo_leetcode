from typing import List

class Solution:
    def cmp_time(self, time1: str, time2: str) -> int:
        if time1 > time2:
            return 1
        elif time1 == time2:
            return 0
        else:
            return -1

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if self.cmp_time(event1[0], event2[1]) in (-1, 0) and self.cmp_time(event2[0], event1[1]) in (-1, 0):
            return True
        return False

