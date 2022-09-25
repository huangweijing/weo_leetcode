from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for num in nums:
            if num & 1 == 0:
                even_sum += num
        result = []
        for query in queries:
            val = query[0]
            idx = query[1]
            if (nums[idx] & 1) == 0 and (val & 1) == 0:
                even_sum += val
            elif (nums[idx] & 1) == 0 and (val & 1) == 1:
                even_sum -= nums[idx]
            elif (nums[idx] & 1) == 1 and (val & 1) == 0:
                pass
            elif (nums[idx] & 1) == 1 and (val & 1) == 1:
                even_sum += val + nums[idx]

            nums[idx] += val
            result.append(even_sum)
        return result