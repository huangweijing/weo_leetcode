from typing import List
import bisect

class Data:
    def __init__(self, val: int, idx: int):
        self.val = val
        self.idx = idx

    def __lt__(self, other):
        return self.val > other.val


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left_part = [Data(nums[k], k)]
        right_part = [Data(nums[k], k)]
        min_num = nums[k]
        for i in reversed(range(k)):
            if nums[i] < min_num:
                left_part.append(Data(nums[i], i))
                min_num = nums[i]
            else:
                left_part[-1].idx = i
        min_num = nums[k]
        for i in range(k, len(nums)):
            if nums[i] < min_num:
                right_part.append(Data(nums[i], i))
                min_num = nums[i]
            else:
                right_part[-1].idx = i
        ans = 0
        for part in left_part:
            idx = bisect.bisect_right(right_part, Data(part.val, -1)) - 1
            if idx == -1:
                val = (k - part.idx + 1) * part.val
            else:
                val = (right_part[idx].idx - part.idx + 1) * part.val
            ans = max(ans, val)
        for part in right_part:
            idx = bisect.bisect_right(left_part, Data(part.val, -1)) - 1
            if idx == -1:
                val = (part.idx - k + 1) * part.val
            else:
                val = (part.idx - left_part[idx].idx + 1) * part.val
            ans = max(ans, val)
        return ans

data = [
    [4, 3, 14, 28, 47, 41, 22, 12, 7]
    , 5
]
r = Solution().maximumScore(* data)
print(r)



# d = [[41, 4], [28, 3], [14, 2], [3, 0]]
# # d = [Data(41, 4), Data(28, 3), Data(14, 2), Data(3, 0)]
# # a = bisect.bisect_left(d, Data(41, 3))
# a = bisect.bisect_left(d, [41, 3], key=lambda x: [x[0]])
# print(a)
