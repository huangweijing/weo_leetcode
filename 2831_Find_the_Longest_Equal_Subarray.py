from typing import List
from collections import deque

class NumInfo:
    def __init__(self):
        self.idx_list = deque()
        self.max_len = 0
        self.need_del = 0


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        info_dict = dict[int, NumInfo]()
        for i, num in enumerate(nums):
            if num not in info_dict:
                num_info = NumInfo()
                num_info.max_len = 1
                num_info.need_del = 0
                num_info.idx_list.append(i)
                info_dict[num] = num_info
            else:
                num_info = info_dict[num]
                num_info.need_del += i - num_info.idx_list[-1] - 1
                num_info.idx_list.append(i)
                while num_info.need_del > k and len(num_info.idx_list) >= 2:
                    first_idx = num_info.idx_list.popleft()
                    num_info.need_del -= (num_info.idx_list[0] - first_idx - 1)
                num_info.max_len = max(num_info.max_len, len(num_info.idx_list))
        ans = 0
        for val in info_dict.values():
            ans = max(val.max_len, ans)

        # for key, val in info_dict.items():
        #     print(f"{key}, {val.idx_list}, {val.need_del}")
        return ans

data = [
    [1, 1, 2, 1, 1]
    , 1
]
r = Solution().longestEqualSubarray(* data)
print(r)


