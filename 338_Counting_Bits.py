from typing import List

def plus1(t: int):
    return t + 1

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits_cnt = [0, 1]
        while len(bits_cnt) < n + 1:
            bits_cnt = bits_cnt + list(map(plus1, bits_cnt.copy()))
        return bits_cnt[: n + 1]
