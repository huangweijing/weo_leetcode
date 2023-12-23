import heapq


class Num:
    def __init__(self, num: float):
        self.num = num

    def __lt__(self, other):
        return self.num > other.num

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sum_all = sum(nums)
        reduced_val = 0
        arr = [Num(num) for num in nums]
        heapq.heapify(arr)
        cnt = 0
        while len(arr) > 0:
            top = heapq.heappop(arr)
            half = top.num / 2
            reduced_val += half
            cnt += 1
            if reduced_val * 2 >= sum_all:
                return cnt
            heapq.heappush(arr, Num(half))
        return -1





