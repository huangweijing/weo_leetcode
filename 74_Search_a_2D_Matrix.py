class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for col in row:
                if matrix[row][col] == target:
                    return True
        return False
        # last_row = None
        # for row in matrix:
        #     if row[0] > target:
        #         if last_row is None:
        #             return False
        #
        #     last_row = row
