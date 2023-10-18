from typing import List
from collections import Counter


class WeoST:
    RANGE = [0, 10 ** 9]
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


class MyCalendarTwo:

    def __init__(self):
        self.st = WeoST()

    def book(self, start: int, end: int) -> bool:
        if self.st.get_max(start, end - 1) < 2:
            self.st.update(start, end - 1, 1)
            return True
        else:
            return False



st = WeoST()
st.update(10, 19, 1)
st.update(50, 59, 1)
st.update(10, 40, 1)
print(st.get_max(5, 14))