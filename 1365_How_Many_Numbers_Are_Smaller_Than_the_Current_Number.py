from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0] * 101
        for num in nums:
            arr[num] += 1
        sum_to_cur = []
        sum_num = 0
        for num in arr:
            sum_num += num
            sum_to_cur.append(sum_num)

        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(sum_to_cur[num - 1])
        return result

data = [
[8,1,2,2,3]
]
r = Solution().smallerNumbersThanCurrent(* data)
print(r)

