from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        idx = 0
        jump_count = 0
        while idx < len(nums):
            if idx == len(nums) - 1:
                return jump_count
            if idx + nums[idx] >= len(nums) - 1:
                return jump_count + 1

            num = nums[idx]
            best_choice = -1
            biggest_step = 0
            for idx2 in range(1, num + 1):
                # print(f"---idx2:{idx2}---")
                if idx2 + idx > len(nums) - 1:
                    best_choice = len(nums) - 1 - idx
                    break
                step = nums[idx2 + idx]
                if step + idx2 > biggest_step:
                    biggest_step = step + idx2
                    best_choice = idx2
                # print(f"---best_choice:{best_choice}, biggest_step:{biggest_step}, jump_count:{jump_count}---")
            # print(nums, idx, idx + best_choice)
            idx += best_choice
            jump_count += 1

sol = Solution()
r = sol.jump([2,3,1])
print(r)