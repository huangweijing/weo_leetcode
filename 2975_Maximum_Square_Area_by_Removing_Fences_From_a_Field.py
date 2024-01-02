class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.sort()
        vFences.sort()
        seq_cnt = 1
        max_vert_seq, max_hor_seq = 1, 1
        for i, bar in enumerate(hFences[1: ], start=1):
            if hFences[i - 1] + 1 == hFences[i]:
                seq_cnt += 1
            else:
                seq_cnt = 1
            max_vert_seq = max(max_vert_seq, seq_cnt)
        seq_cnt = 1
        for i, bar in enumerate(vFences[1: ], start=1):
            if vFences[i - 1] + 1 == vFences[i]:
                seq_cnt += 1
            else:
                seq_cnt = 1
            max_hor_seq = max(max_hor_seq, seq_cnt)
        side = min(max_hor_seq, max_vert_seq)
        return (side + 1) ** 2