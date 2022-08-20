from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt_dict = dict[int, int]()
        for num in nums:
            if num not in cnt_dict:
                cnt_dict[num] = 0
            cnt_dict[num] += 1

        key_list = list(cnt_dict.keys())
        key_list.sort()

        lhs = 0
        for i in range(1, len(key_list)):
            if key_list[i] - key_list[i - 1] > 1:
                continue
            else:
                hs = cnt_dict[key_list[i]] + cnt_dict[key_list[i - 1]]
                if hs > lhs:
                    lhs = hs
        return lhs

