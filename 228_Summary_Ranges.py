from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = list[str]()
        i = 0
        while i < len(nums):
            start_num = nums[i]
            end_num = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[j - 1] == 1:
                    end_num = nums[j]
                    i = j
                else:
                    break
            if start_num == end_num:
                result.append(str(start_num))
            else:
                result.append(f"{start_num}->{end_num}")
            i += 1
        return result

