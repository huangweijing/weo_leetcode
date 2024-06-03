from typing import List
from collections import Counter, defaultdict


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        ans = 0
        pos_cnt_dict = defaultdict(lambda: Counter())
        for num in nums:
            num_str = str(num)
            for i, ch in enumerate(num_str):
                ch_val = int(ch)
                for val, cnt in pos_cnt_dict[i].items():
                    if val != ch_val:
                        ans += cnt
                pos_cnt_dict[i][ch_val] += 1
        return ans


data = [50,28,48]
r = Solution().sumDigitDifferences(data)
print(r)