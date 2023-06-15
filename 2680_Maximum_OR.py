from typing import List
from collections import Counter

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        bit_cnt = Counter()
        max_bit_cnt = 0
        for num in nums:
            bit_stk = list(bin(num)[2:])
            max_bit_cnt = max(max_bit_cnt, len(bit_stk))
            bit_idx = 0
            while len(bit_stk) > 0:
                if bit_stk.pop() == "1":
                    bit_cnt[bit_idx] += 1
                bit_idx += 1
        or_all_val = 0
        for bit_idx in bit_cnt.keys():
            or_all_val += (1 << bit_idx)

        ans = or_all_val
        for num in nums:
            bit_cnt_copy = bit_cnt.copy()
            bit_stk = list(bin(num)[2:])
            if len(bit_stk) != max_bit_cnt:
                continue
            bit_idx = 0
            while len(bit_stk) > 0:
                if bit_stk.pop() == "1":
                    bit_cnt_copy[bit_idx] -= 1
                    if bit_cnt_copy[bit_idx] == 0:
                        del bit_cnt_copy[bit_idx]
                bit_idx += 1
            new_num = num << k
            bit_stk = list(bin(new_num)[2:])
            bit_idx = 0
            while len(bit_stk) > 0:
                if bit_stk.pop() == "1":
                    bit_cnt_copy[bit_idx] += 1
                bit_idx += 1
            # print(new_num, bit_cnt_copy)

            new_or_all_val = 0
            for bit_idx in bit_cnt_copy.keys():
                new_or_all_val += (1 << bit_idx)

            ans = max(ans, new_or_all_val)
        return ans

data = [
    [8, 1, 2]
    , 2
]
r = Solution().maximumOr(* data)
print(r)