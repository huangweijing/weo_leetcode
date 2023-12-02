from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int
                               , hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        seq_cnt = 1
        max_vert_seq, max_hor_seq = 1, 1
        for i, bar in enumerate(hBars[1: ], start=1):
            if hBars[i - 1] + 1 == hBars[i]:
                seq_cnt += 1
            else:
                seq_cnt = 1
            max_vert_seq = max(max_vert_seq, seq_cnt)
        seq_cnt = 1
        for i, bar in enumerate(vBars[1: ], start=1):
            if vBars[i - 1] + 1 == vBars[i]:
                seq_cnt += 1
            else:
                seq_cnt = 1
            max_hor_seq = max(max_hor_seq, seq_cnt)
        side = min(max_hor_seq, max_vert_seq)
        return (side + 1) ** 2


data = [
    2
    , 1
    , [2,3]
    , [2]
]
r = Solution().maximizeSquareHoleArea(* data)
print(r)