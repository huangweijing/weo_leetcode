from typing import List

class Solution:
    def can_find_num(self, numbers: List[int], num: int, myself_idx: int):
        left_wall = 0
        right_wall = len(numbers)
        idx = (left_wall + right_wall) >> 1
        while True:
            # print(numbers, left_wall, right_wall, idx, myself_idx)
            # print(numbers[idx])
            if idx == myself_idx:
                idx += 1
            if numbers[idx] == num:
                return idx
            elif numbers[idx] > num:
                right_wall = idx
            elif numbers[idx] < num:
                left_wall = idx
            # print(left_wall, right_wall, idx, num)
            idx = (left_wall + right_wall) >> 1


            if idx == len(numbers) - 1 and numbers[idx] < num:
                return None
            if idx == 0 and num < numbers[idx]:
                return None
            if idx < len(numbers) - 1 and numbers[idx] < num < numbers[idx + 1]:
                return None
        return None


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            # print(idx, num)
            sec_num = target - num
            # if sec_num == num:
            #     continue
            sec_num_idx = self.can_find_num(numbers, sec_num, idx)
            if sec_num_idx is not None:
                return [idx + 1, sec_num_idx + 1]
            # print("----")
        return []

sol = Solution()
r = sol.twoSum([1,3,4,4], 8)
print(r)
