from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        h = len(nums)
        result = []
        # last_len = -1
        last_len_mapping = dict[int, int]()
        for i in range(h):
            last_len = len(nums[i]) - ((h - 1) - i)
            last_len_mapping[i] = last_len

        for i in range(h):
            row, col = i, 0
            while row >= 0:
                if col < len(nums[row]):
                    result.append(nums[row][col])
                col += 1
                row -= 1
            last_len = max(len(nums[i]) - ((h - 1) - i), last_len)
            # print(last_len, ((h - 1) - i))

        for i in range(1, last_len):
            row, col = h - 1, i
            while row >= 0:
                if col < len(nums[row]):
                    result.append(nums[row][col])
                col += 1
                row -= 1
        return result

data_nums = [[1,2,3,4,5],[6,7],[8],[12,13,14,15,16],[9,10,11]]
r = Solution().findDiagonalOrder(data_nums)
print(r)
