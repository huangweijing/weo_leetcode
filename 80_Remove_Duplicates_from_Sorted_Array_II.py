from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_num = None
        update_idx = 0
        for idx in range(len(nums)):
            if cur_num != nums[idx]:
                cur_num = nums[idx]
                new_num_flg = True
            else:
                new_num_flg = False

            if new_num_flg:
                jump_idx = idx + 1
                while jump_idx < len(nums) and nums[jump_idx] == cur_num:
                    jump_idx += 1
                if jump_idx - idx >= 2:
                    copy_cnt = 2
                else:
                    copy_cnt = 1
                for i in range(copy_cnt):
                    nums[update_idx] = cur_num
                    update_idx += 1

        return update_idx

data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 8, 8, 9]
r = Solution().removeDuplicates(data)
print(data, r)



