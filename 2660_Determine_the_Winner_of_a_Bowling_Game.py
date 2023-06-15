from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1, score2 = 0, 0

        ten_round1, ten_round2 = -1, -1
        for i in range(len(player1)):
            score1 += player1[i]
            if ten_round1 != -1 and (ten_round1 + 2 == i or ten_round1 + 1 == i):
                score1 += player1[i]
            if player1[i] == 10:
                ten_round1 = i

            score2 += player2[i]
            if ten_round2 != -1 and (ten_round2 + 2 == i or ten_round2 + 1 == i):
                score2 += player2[i]
            if player2[i] == 10:
                ten_round2 = i

        return 0 if score1 == score2 else 1 if score1 > score2 else 2


data = [
    [5,6,1,10]
    , [5,1,10,5]
]
r = Solution().isWinner(* data)
print(r)