from typing import List
from collections import Counter


class WeoST:
    RANGE = [1, 10 ** 9]
    def __init__(self):
        self.val = Counter()
        # self.lazy = Counter()

    def update(self, start: int, end: int, val: int, left: int = RANGE[0]
               , right: int = RANGE[1], node: int = 1):
        if start > right or end < left:
            return
        if start <= left and end >= right:
            # print(f"set node({node})={self.val[node]}+{val}")
            # self.lazy[node] += val
            self.val[node] += val
        else:
            mid = left + right >> 1
            # if node * 2 not in self.val:
            self.val[node * 2] += self.val[node]
            self.val[node * 2 + 1] += self.val[node]
            # print(f"split:{node}->({node * 2}, {node * 2 + 1})", self.val)
            self.val[node] = 0
            self.update(start, end, val, left, mid, node * 2)
            self.update(start, end, val, mid + 1, right, node * 2 + 1)


    def get(self, pos: int, left: int = RANGE[0]
            , right: int = RANGE[1], node: int = 1) -> int:
        # print(pos, left, right)
        if pos > right or pos < left:
            return -1
        mid = left + right >> 1
        if pos <= mid:
            if node * 2 not in self.val:
                return self.val[node]
            else:
                return self.get(pos, left, mid, node * 2) + self.val[node]
        else:
            if node * 2 + 1 not in self.val:
                return self.val[node]
            else:
                return self.get(pos, mid + 1, right, node * 2 + 1) + self.val[node]


    def get_max(self, start: int, end: int
                , left: int = RANGE[0], right: int = RANGE[1], node: int = 1) -> int:
        # print("get_max", left, right)
        if start > right or end < left:
            return -1

        mid = left + right >> 1
        if start <= left and end >= right:
            if node * 2 in self.val:
                m1 = self.get_max(start, end, left, mid, node * 2)
                m2 = self.get_max(start, end, mid + 1, right, node * 2 + 1)
                return max(m1, m2) + self.val[node]
            else:
                return self.val[node]
        else:
            m1 = self.get_max(start, end, left, mid, node * 2)
            m2 = self.get_max(start, end, mid + 1, right, node * 2 + 1)
            return max(m1, m2) + self.val[node]

wst = WeoST()
wst.update(1, 10, 3)
wst.update(1, 20, 5)
print(wst.get(8))
# print(wst.val)
wst.update(51, 58, 2)
print(wst.get(59))
# print(wst.val)