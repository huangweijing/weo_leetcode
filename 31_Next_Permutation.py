from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 1
        while idx >= 0:
            smallest_bigger_val = 101
            smallest_bigger_idx = -1
            for bigger_idx in range(idx + 1, len(nums)):
                if nums[bigger_idx] > nums[idx]:
                    if nums[bigger_idx] < smallest_bigger_val:
                        smallest_bigger_idx = bigger_idx
                        smallest_bigger_val = nums[bigger_idx]
            if smallest_bigger_idx == -1:
                idx -= 1
                continue
            else:
                shuffle_list = list[int]()
                for idx2 in range(idx, len(nums)):
                    shuffle_list.append(nums[idx2])
                shuffle_list.remove(smallest_bigger_val)
                shuffle_list.sort()
                # print(f"shuffle_list={shuffle_list}, idx={idx}")
                nums[idx] = smallest_bigger_val
                for i in range(1, len(nums) - idx):
                    # print(f"i={i}, idx={idx}")
                    nums[idx + i] = shuffle_list[i - 1]
                return
        nums.sort()

sol = Solution()
num_arr = [3, 2, 1]
sol.nextPermutation(num_arr)
print(num_arr)