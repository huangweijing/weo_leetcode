from typing import List
from collections import defaultdict


class Solution:
    def count_group(self, seat: int) -> int:
        if seat & 0b0111111110 == 0:
            return 2
        if seat & 0b0111100000 == 0 or seat & 0b0000011110 == 0:
            return 1
        if seat & 0b0001111000 == 0:
            return 1
        return 0

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seat_dict = defaultdict(lambda: list[int]())
        for seat in reservedSeats:
            seat_dict[seat[0]].append(seat[1])
        ans = 0
        for seats in seat_dict.values():
            val = 0
            for seat in seats:
                val |= 1 << (seat - 1)
            # print(bin(val)[2:].rjust(10, "0"), self.count_group(val))
            ans += self.count_group(val)
        ans += (n - len(seat_dict)) * 2
        return ans
    

data = [
    3
    , [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
]
r = Solution().maxNumberOfFamilies(*data)
print(r)
        