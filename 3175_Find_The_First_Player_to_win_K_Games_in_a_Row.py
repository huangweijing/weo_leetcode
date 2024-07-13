from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        remain_game_cnt = k
        cur_winner = 0
        for i, skill in enumerate(skills[1:], start=1):
            if skill > skills[cur_winner]:
                cur_winner = i
                remain_game_cnt = k - 1
            else:
                remain_game_cnt -= 1
            if remain_game_cnt == 0:
                return cur_winner
        return cur_winner


data = [
    [2, 5, 4]
    , 3
]
r = Solution().findWinningPlayer(* data)
print(r)