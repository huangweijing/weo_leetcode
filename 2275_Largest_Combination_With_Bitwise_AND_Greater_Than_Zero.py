from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_bit = 25
        bit_len = [0] * 25
        for cand in candidates:
            for i in range(max_bit):
                bit_len[i] += 1 if cand & (1 << i) != 0 else 0
        return max(bit_len)

