from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr = list(set(arr))
        new_arr.sort()
        rank_dict = { num: i + 1 for i, num in enumerate(new_arr)  }
        return list(map(rank_dict.get, arr))
