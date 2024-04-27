from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piece_dict = dict[int, list[int]]()
        for p in pieces:
            piece_dict[p[0]] = p
        idx = 0
        # print(piece_dict)
        while idx < len(arr):
            if arr[idx] not in piece_dict:
                return False
            piece = piece_dict[arr[idx]]
            for val in piece:
                if arr[idx] != val:
                    return False
                idx += 1
        return True


data = [
    [15,88]
    , [[88],[15]]
]
r = Solution().canFormArray(* data)
print(r)


