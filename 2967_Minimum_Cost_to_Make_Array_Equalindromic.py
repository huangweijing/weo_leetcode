from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        avg = nums[len(nums) >> 1]
        str_avg = str(avg)
        str_half = str_avg[: (len(str_avg) + 1) >> 1]
        # print(str_half)
        if len(str_avg) % 2 == 0:
            v1 = int(str_half + str_half[::-1])
        else:
            v1 = int(str_half[:-1] + str_half[::-1])
        int_half = int(str_half)
        str_plus = str(int_half + 1)
        if len(str_avg) % 2 == 0:
            v2 = int(str_plus + str_plus[::-1])
        else:
            v2 = int(str_plus[:-1] + str_plus[::-1])
        str_min = str(int_half - 1)
        if len(str_avg) % 2 == 0:
            v3 = int(str_min + str_min[::-1])
        else:
            v3 = int(str_min[:-1] + str_min[::-1])
        # print(v1, v2, avg)
        # print(sum(map(lambda x: abs(x - 313), nums)))
        return min(sum(map(lambda x: abs(x - v2), nums))
            , sum(map(lambda x: abs(x - v1), nums))
            , sum(map(lambda x: abs(x - v3), nums)))

data = [311,313,320,324]
# data = [14,25,31,41,103]
r = Solution().minimumCost(data)
print(r)
