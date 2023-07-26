from typing import List

class Solution:
    def countBlackBlocks(self, m: int, n: int
                         , coordinates: List[List[int]]) -> List[int]:
        coord_set = set[int]()
        for coordinate in coordinates:
            coord_set.add(coordinate[0] * n + coordinate[1])
        ans_set = [set(), set(), set(), set(), set()]
        offset_arr = [[-1, -1], [-1, 0], [0, -1], [0, 0]]
        block_arr = [[0, 0], [0, 1], [1, 0], [1, 1]]
        # print(coord_set)
        for coordinate in coordinates:
            row, col = coordinate[0], coordinate[1]
            for offset in offset_arr:
                is_offset_okay = True
                block_count = 0
                block_store = []
                for block in block_arr:
                    block_row = row + offset[0] + block[0]
                    block_col = col + offset[1] + block[1]
                    if not (0 <= block_row < m and 0 <= block_col < n):
                        is_offset_okay = False
                        break
                    if block_row * n + block_col in coord_set:
                        block_count += 1
                    block_store.append([block_row, block_col])
                if is_offset_okay:
                    # print(row + offset[0], col + offset[1], f"block_cnt={block_count}, block_store={block_store}")
                    ans_set[block_count].add((row + offset[0]) * n + (col + offset[1]))

        ans = [(m - 1) * (n - 1) - sum([len(x) for x in ans_set]), len(ans_set[1])
               , len(ans_set[2]), len(ans_set[3]), len(ans_set[4])]
        return ans

data = [
    13
    , 40
    , [[10, 0], [1, 11], [10, 2], [10, 23], [10, 11], [12, 39]]
]
r = Solution().countBlackBlocks(* data)
print(r)



