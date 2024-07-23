from typing import List
from sortedcontainers import SortedList
from collections import Counter


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        ans = []
        sl = SortedList(key=lambda x: (x[1], x[0]))
        num_freq = Counter()
        for i in range(len(nums)):
            num, f = nums[i], freq[i]
            orig = [num, num_freq[num]]
            idx = sl.bisect_right(orig) - 1
            if idx != -1 and sl[idx] == orig:
                sl.remove(orig)
                sl.add([num, orig[1] + f])
            else:
                sl.add([num, f])
            num_freq[num] += f
            ans.append(sl[-1][1])
        return ans