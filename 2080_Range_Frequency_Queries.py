from typing import List
import bisect

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.val_tbl = dict[int, list[int]]()
        for i, n in enumerate(arr):
            if n not in self.val_tbl:
                self.val_tbl[n] = list[int]()
            self.val_tbl[n].append(i)
        # print(self.val_tbl)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.val_tbl:
            return 0
        idx_list = self.val_tbl[value]
        left_idx = bisect.bisect_left(idx_list, left)
        right_idx = bisect.bisect_right(idx_list, right)
        # print(idx_list, left_idx, right_idx)
        return right_idx - left_idx

data = [12,33,4,56,22,2,34,33,22,12,34,56]
rfq = RangeFreqQuery(data)
r = rfq.query(0, 11, 33)
print(r)
