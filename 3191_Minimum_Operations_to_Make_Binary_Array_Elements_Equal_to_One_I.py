from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        flip_info = [0, 0]
        for i, num in enumerate(nums):
            # print(num, flip_info)
            new_flip_info = [0, flip_info[0]]
            if num ^ (sum(flip_info) & 1) == 0:
                # print("flip!")
                if i >= len(nums) - 2:
                    return -1
                new_flip_info[0] = 1
                ans += 1
            flip_info = new_flip_info
        return ans


data = [0,1,1,1,0,0]
r = Solution().minOperations(data)
print(r)