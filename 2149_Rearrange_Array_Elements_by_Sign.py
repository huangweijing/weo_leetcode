from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_idx = 0
        neg_idx = 1
        result = [0] * len(nums)
        for num in nums:
            if num < 0:
                result[neg_idx] = num
                neg_idx += 2
            else:
                result[pos_idx] = num
                pos_idx += 2
        return result

data_nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
r = Solution().rearrangeArray(data_nums)
print(r)