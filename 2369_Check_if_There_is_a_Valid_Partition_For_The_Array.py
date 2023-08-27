from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        pat = [None] * 8
        # ch2_1, ch2_2, ch3_1, ch3_2, ch3_3, in3_1, in3_2, in3_3
        num = nums[0]
        pat[0], pat[2], pat[5] = num, num, num
        for num in nums[1:]:
            new_stat = False
            new_pat = [None] * 8
            if pat[1] is not None or pat[4] is not None or pat[7] is not None:
                new_pat[0], new_pat[2], new_pat[5] = num, num, num
                new_stat = True
            if pat[0] == num:
                new_pat[1] = num
                new_stat = True
            if pat[2] == num:
                new_pat[3] = num
                new_stat = True
            if pat[3] == num:
                new_pat[4] = num
                new_stat = True
            if pat[5] == num - 1:
                new_pat[6] = num
                new_stat = True
            if pat[6] == num - 1:
                new_pat[7] = num
                new_stat = True
            pat = new_pat
            if not new_stat:
                return False
        if pat[1] is not None or pat[4] is not None or pat[7] is not None:
            return True
        return False
