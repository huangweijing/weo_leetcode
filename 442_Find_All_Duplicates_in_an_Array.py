from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        idx = 0
        while idx < len(nums):
            # print(nums)
            if nums[idx] == idx + 1:
                idx += 1
                continue

            cur = idx
            while nums[cur] - 1 != cur:
                new_cur = nums[cur] - 1
                if nums[cur] == nums[new_cur]:
                    # result.append(nums[cur])
                    break
                # print(f"exchange idx:{cur}={nums[cur]}, {new_cur}={nums[new_cur]}")
                nums[cur], nums[new_cur] = nums[new_cur], nums[cur]
                # cur = new_cur
            idx += 1

        for i, num in enumerate(nums):
            if i + 1 != num:
                result.append(num)
        return result

r = Solution().findDuplicates([4,3,2,7,8,2,3,1])
print(r)



