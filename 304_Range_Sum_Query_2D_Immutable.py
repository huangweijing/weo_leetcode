from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sum_left = [[0] * len(matrix[0]) for i in range(len(matrix))]
        self.sum_left_top = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for row in range(len(matrix)):
            sum_result = 0
            for col in range(len(matrix[0])):
                sum_result += matrix[row][col]
                self.sum_left[row][col] = sum_result

        for col in range(len(matrix[0])):
            sum_result = 0
            for row in range(len(matrix)):
                sum_result += self.sum_left[row][col]
                self.sum_left_top[row][col] = sum_result

        print(self.sum_left_top)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        main_sum = self.sum_left_top[row2][col2]
        if row1 > 0:
            top_sum = self.sum_left_top[row1 - 1][col2]
        else:
            top_sum = 0
        if col1 > 0:
            left_sum = self.sum_left_top[row2][col1 - 1]
        else:
            left_sum = 0
        if row1 > 0 and col1 > 0:
            left_top_sum = self.sum_left_top[row1 - 1][col1 - 1]
        else:
            left_top_sum = 0
        return main_sum - left_sum - top_sum + left_top_sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = NumMatrix([[1] * 10 for i in range(3)])
print(matrix.sumRegion(1, 1, 2, 2))