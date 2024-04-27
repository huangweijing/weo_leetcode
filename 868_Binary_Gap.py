class Solution:
    def binaryGap(self, n: int) -> int:
        last_one_idx = -1
        idx = 0
        ans = 0
        while n > 0:
            b = n & 1
            n >>= 1
            if last_one_idx != -1 and b == 1:
                ans = max(ans, idx - last_one_idx)
            if b == 1:
                last_one_idx = idx
            idx += 1
        return ans




