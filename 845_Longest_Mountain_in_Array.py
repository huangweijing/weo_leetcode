from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        inc_len_arr = [0] * len(arr)
        dec_len_arr = [0] * len(arr)
        inc_len_arr[-1], inc_len_arr[0] = 1, 1
        dec_len_arr[-1], dec_len_arr[0] = 1, 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                inc_len_arr[i] = inc_len_arr[i - 1] + 1
            else:
                inc_len_arr[i] = 1
        ans = 0
        for i in range(1, len(arr)):
            if arr[-1 - i] > arr[-1 - (i - 1)]:
                dec_len_arr[-1 - i] = dec_len_arr[-1 - (i - 1)] + 1
            else:
                dec_len_arr[-1 - i] = 1
            width = inc_len_arr[-1 - i] + dec_len_arr[-1 - i] - 1
            if width < 3 or inc_len_arr[-1 - i] == 1 or dec_len_arr[-1 - i] == 1:
                width = 0
            ans = max(width, ans)
        return ans


