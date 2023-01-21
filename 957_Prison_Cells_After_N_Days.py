from typing import List
from collections import deque

class Solution:
    def __init__(self):
        self.state_rnd = dict[int, int]()
        self.state_loop = dict[int, int]()

    def bin_to_dec(self, cells: list[int]):
        cells = deque(cells.copy())
        ans = 0
        while len(cells) > 0:
            ans <<= 1
            ans += cells.popleft()
        return ans

    def dec_to_bin(self, state: int) -> list[int]:
        cells = deque()
        while state > 0:
            cells.appendleft(state & 1)
            state >>= 1
        while len(cells) < 8:
            cells.appendleft(0)
        return cells

    def next_state(self, state: list[int]) -> list[int]:
        new_state = [0] * len(state)
        for i in range(len(state)):
            n1, n2 = 0, 0
            if i > 0:
                n1 = state[i - 1]
            if i < len(state) - 1:
                n2 = state[i + 1]
            if 0 < i < len(state) - 1:
                new_state[i] = 1 - (n1 ^ n2)
        return new_state

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        state = cells
        day = 0
        while day < n:
            # print(day, state)
            int_state = self.bin_to_dec(state)
            if int_state not in self.state_rnd:
                self.state_rnd[int_state] = day
            else:
                self.state_loop[int_state] = day - self.state_rnd[int_state]
            if int_state in self.state_loop:
                loop_cnt = self.state_loop[int_state]
                if n >= loop_cnt + day:
                    day = n - (n - day) % loop_cnt
                    if day == n:
                        return state
            state = self.next_state(state)
            day += 1
        return state

data = [
    [1,0,0,0,1,0,0,1]
    , 99
]
r = Solution().prisonAfterNDays(* data)
print(r)



# print(Solution().bin_to_dec([0, 0, 0, 0, 1, 0, 1, 0]))
# print(Solution().dec_to_bin(10))
# state = [0,1,0,1,1,0,0,1]
# s = Solution()
# i = 0
# sta_tbl = [-1] * 200
# while i < 1000:
#     new_state = s.next_state(state)
#     print(s.bin_to_dec(state), s.bin_to_dec(new_state))
#     sta_tbl[s.bin_to_dec(state)] = s.bin_to_dec(new_state)
#     state = new_state
#     i += 1
# print(sta_tbl)
