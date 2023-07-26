class Solution:
    JUMP_VEC = [
        [1, 2]
        , [1, -2]
        , [-1, 2]
        , [-1, -2]
        ,[2, 1]
        , [2, -1]
        , [-2, 1]
        , [-2, -1]
    ]

    def next(self, board: list[list[int]]) -> list[list[int]]:
        n = len(board)
        board_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for step in Solution.JUMP_VEC:
                    from_row = i + step[0]
                    from_col = j + step[1]
                    if 0 <= from_row < n and 0 <= from_col < n:
                        board_new[i][j] += board[from_row][from_col] * 0.125
        return board_new


    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        board = [[0] * n for _ in range(n)]
        board[row][column] = 1
        for i in range(k):
            board = self.next(board)
        ans = 0
        for row_data in board:
            for prob in row_data:
                ans += prob
        return ans

data = [
1
, 0
, 0
, 0
]
r = Solution().knightProbability(* data)
print(r)
