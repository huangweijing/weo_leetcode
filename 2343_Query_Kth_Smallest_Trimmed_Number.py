from typing import List
from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def build(self, nums: list[str], trim):
        ret = SortedList(key=lambda x: x[1])
        for i, num in enumerate(nums):
            ret.add([i, num[-trim:]])
        return ret

    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        trim_tbl = defaultdict(lambda: SortedList())
        ans = []
        for query in queries:
            k = query[0]
            trim = query[1]
            if trim not in trim_tbl:
                trimmed_list = self.build(nums, trim)
                trim_tbl[query[1]] = trimmed_list
            ans.append(trim_tbl[query[1]][k - 1][0])
        return ans


