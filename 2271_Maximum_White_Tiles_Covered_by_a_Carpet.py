import itertools
from typing import List
import bisect


class Tile:
    def __init__(self, l: int, r: int):
        self.l, self.r = l, r
        self.len = r - l + 1

    def __lt__(self, other):
        return self.l < other.l or \
               (self.l == other.l and self.r < other.r)


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # print(tiles)
        tile_list = list[Tile]()
        for i, tile in enumerate(tiles):
            tile_list.append(Tile(tile[0], tile[1]))
        tile_list.sort()

        prefix_sum_arr = [0] * len(tiles)
        prefix_sum = 0
        for i, tile in enumerate(tile_list):
            prefix_sum_arr[i] = prefix_sum
            prefix_sum += tile.r - tile.l + 1
        prefix_sum_arr.append(prefix_sum)

        # print(prefix_sum_arr)

        ans = 0
        for i, tile in enumerate(tile_list):
            idx = bisect.bisect_right(tile_list, Tile(tile.l + carpetLen - 1, 10 ** 9 + 1)) - 1
            found_tile = tile_list[idx]
            found_tile_covered = min(tile.l + carpetLen - found_tile.l, found_tile.len)
            ans = max(prefix_sum_arr[idx] - prefix_sum_arr[i] \
                                + found_tile_covered, ans)
            # print(f"i={i}, tile.l={tile.l}, tile.r={tile.r}"
            #       f", idx={idx}, ft.l={found_tile.l}, ft.r={found_tile.r}"
            #       f", ft_covered={found_tile_covered} ans={ans}")
        ans = 0
        for i, tile in enumerate(tile_list):
            idx = bisect.bisect_right(tile_list, Tile(tile.r - carpetLen + 1, 0)) - 1
            if idx == -1:
                ans = max(prefix_sum_arr[i] + tile.len, ans)
                # print(f"i={i}, tile.l={tile.l}, tile.r={tile.r}, ans={ans}")
            else:
                found_tile = tile_list[idx]
                found_tile_not_covered = min(tile.r - carpetLen + 1 - found_tile.l, found_tile.len)
                ans = max(tile.len + prefix_sum_arr[i] \
                          - prefix_sum_arr[idx] - found_tile_not_covered, ans)
                # print(f"i={i}, tile.l={tile.l}, tile.r={tile.r}"
                #       f", idx={idx}, ft.l={found_tile.l}, ft.r={found_tile.r}"
                #       f", ft_not_covered={found_tile_not_covered} ans={ans}")
        return ans

data = [
    [[10,11],[1,1]]
    , 2
]
res = Solution().maximumWhiteTiles(* data)
print(res)
