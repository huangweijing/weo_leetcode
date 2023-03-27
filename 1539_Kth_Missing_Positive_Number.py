from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        idx = 0
        missing_cnt = 0
        for i in range(1, 2001):
            if idx < len(arr) and arr[idx] == i:
                idx += 1
            else:
                missing_cnt += 1
            if missing_cnt == k:
                return i
        return -1


