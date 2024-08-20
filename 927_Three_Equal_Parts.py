from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        one_cnt = 0
        for num in arr:
            if num == 1:
                one_cnt += 1
        if one_cnt == 0:
            return [0, len(arr) - 1]
        if one_cnt % 3 != 0:
            return [-1, -1]
        left_range = [1, one_cnt // 3]
        middle_range = [one_cnt // 3 + 1, 2 * one_cnt // 3]
        right_range = [2 * one_cnt // 3 + 1, one_cnt]
        left, middle, right = [-1, -1], [-1, -1], [-1, -1]
        ones = 0
        for i, num in enumerate(arr):
            if num == 1:
                ones += 1
            if left_range[0] == ones and left[0] == -1:
                left[0] = i
            if left_range[1] == ones and left[1] == -1:
                left[1] = i
            if middle_range[0] == ones and middle[0] == -1:
                middle[0] = i
            if middle_range[1] == ones and middle[1] == -1:
                middle[1] = i
            if right_range[0] == ones and right[0] == -1:
                right[0] = i
            if right_range[1] == ones and right[1] == -1:
                right[1] = i
                
        # print(left_range, middle_range, right_range)
        # print(left, middle, right)
        # (3) part > (2) part
        if len(arr) - 1 - right[1] > right[0] - middle[1] - 1:
            return [-1, -1]
        # (3) part > (2) part
        if len(arr) - 1 - right[1] > middle[0] - left[1] - 1:
            return [-1, -1]
        for i in range(left[1] - left[0] + 1):
            if arr[left[0] + i] == arr[middle[0] + i] == arr[right[0] + i]:
                continue
            else:
                return [-1, -1]
        return [left[1] + len(arr) - 1 - right[1], middle[1] + len(arr) - 1 - right[1] + 1]


data = [1,1,0,0,1]
r = Solution().threeEqualParts(data)
print(r)