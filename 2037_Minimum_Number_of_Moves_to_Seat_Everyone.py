from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        while len(seats) > 0:
            ans += abs(seats.pop() - students.pop())
        return ans
