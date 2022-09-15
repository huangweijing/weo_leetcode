from typing import List
import bisect

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        sum_arr = []
        sum_num = 0
        for num in arr:
            sum_num += num
            sum_arr.append(sum_num)

        if sum_num % 3 != 0:
            return False

        mini_sect, mini_sect_idx = int(sum_num / 3), -1
        mini_sect2, mini_sect2_idx = mini_sect * 2, -1
        mini_sect3_idx = len(arr) - 1

        for i, sum_num in enumerate(sum_arr):
            if sum_num == mini_sect and mini_sect_idx == -1:
                mini_sect_idx = i
            if sum_num == mini_sect2 and mini_sect_idx not in (-1, i) and mini_sect2_idx == -1:
                mini_sect2_idx = i

        # print(mini_sect_idx , mini_sect2_idx , mini_sect3_idx)
        if mini_sect_idx < mini_sect2_idx < mini_sect3_idx:
            return True

        return False

data = [0,0,0,0]
r = Solution().canThreePartsEqualSum(data)
print(r)
