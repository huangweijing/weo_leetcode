import bisect
from typing import List

class Solution:

    # def my_search_matrix(self, matrix, start_row, start_col, end_row, end_col, target) -> bool:
    #     print(f"my_search_matrix(self, matrix, {start_row}, {start_col}, {end_row}, {end_col}, {target})")
    #
    #     if start_row < 0 or end_row >= len(matrix):
    #         return False
    #     if start_col < 0 or end_col >= len(matrix[0]):
    #         return False
    #
    #     row_count = end_row + 1 - start_row
    #     col_count = end_col + 1 - start_col
    #     diag_count = min(row_count, col_count)
    #     high_idx = diag_count
    #     low_idx = 0
    #     try_idx = (high_idx + low_idx) >> 1
    #     print(f"before loop, {low_idx}, {high_idx}, {diag_count}")
    #     while low_idx <= try_idx <= high_idx:
    #         print(low_idx, high_idx, diag_count, target, matrix[start_row + try_idx][start_col + try_idx])
    #         if matrix[start_row + try_idx][start_col + try_idx] == target:
    #             print(f"found it! ({start_row + try_idx}, {start_col + try_idx})")
    #             return True
    #         if matrix[start_row + try_idx - 1][start_col + try_idx - 1] < target < \
    #                 matrix[start_row + try_idx][start_col + try_idx]:
    #             try_idx = try_idx - 1
    #             break
    #         if matrix[start_row + try_idx][start_col + try_idx] > target:
    #             if try_idx == 0:
    #                 return False
    #             high_idx = try_idx
    #             try_idx = (high_idx + low_idx) >> 1
    #             continue
    #         if matrix[start_row + try_idx][start_col + try_idx] < target:
    #             if try_idx + 1 == diag_count:
    #                 # if width == height False
    #                 if row_count == col_count:
    #                     print("why end!?")
    #                     return False
    #                 elif row_count > col_count:
    #                     print(f"row cnt > col count")
    #                     # if width > height
    #                     return self.my_search_matrix(matrix, start_row + try_idx + 1, start_col
    #                                                  , end_row, end_col, target)
    #                 else:
    #                     # if width < height
    #                     print(f"row cnt < col count")
    #                     return self.my_search_matrix(matrix, start_row, start_col + try_idx + 1
    #                                                  , end_row, end_col, target)
    #             low_idx = try_idx
    #             try_idx = (high_idx + low_idx) >> 1
    #             continue
    #
    #     print(try_idx, try_idx)
    #     return self.my_search_matrix(matrix, start_row + try_idx + 1, start_col
    #                             , end_row, start_col + try_idx, target) or \
    #            self.my_search_matrix(matrix, start_row, start_col + try_idx + 1
    #                             , start_row + try_idx, end_col, target)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx >= len(row):
                continue
            if row[idx] == target:
                return True
        return False

# r = Solution().my_search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]] #,[20,23,25,27,28]
#                             , 0, 0, 4, 4, 24)
# r = Solution().my_search_matrix([[1,4,7,11,15]]
#                             , 0, 0, 0, 4, 24)
r = Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 31)
print(r)
