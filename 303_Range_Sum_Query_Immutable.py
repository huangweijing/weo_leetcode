from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_from_head = list[int]()
        s = 0
        for num in nums:
            s += num
            self.sum_from_head.append(s)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_from_head[right]
        else:
            return self.sum_from_head[right] - self.sum_from_head[left - 1]