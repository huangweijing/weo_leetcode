from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghost_dist = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if ghost_dist <= distance:
                return False
        return True


data = [
    [[1,9],[2,-5],[3,8],[9,8],[-1,3]]
    , [8,-10]
]
r = Solution().escapeGhosts(* data)
print(r)