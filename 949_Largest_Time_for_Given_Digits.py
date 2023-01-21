from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def valid_time_format(self, hh: int, mm: int) -> bool:
        if 0 <= hh <= 23 and 0 <= mm <= 59:
            return True
        else:
            return False

    def comb(self, num_list: list[int]) -> list[list[int]]:
        if len(num_list) == 1:
            return [list(num_list)]
        ans = []
        for num in num_list:
            num_list_copy = num_list.copy()
            num_list_copy.remove(num)
            sub_ans = self.comb(num_list_copy)
            for sub in sub_ans:
                result = list[int]()
                result.append(num)
                result.extend(sub)
                ans.append(result)
        return ans

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        comb_list = self.comb(arr)
        ans = ""
        for comb_arr in comb_list:
            if self.valid_time_format(comb_arr[0] * 10 + comb_arr[1]
                              , comb_arr[2] * 10 + comb_arr[3]):
                ans = max(f"{comb_arr[0]}{comb_arr[1]}:{comb_arr[2]}{comb_arr[3]}", ans)
        return ans

r = Solution().largestTimeFromDigits([3, 1, 5, 4])
print(r)
