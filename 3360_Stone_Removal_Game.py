class Solution:
    def canAliceWin(self, n: int) -> bool:
        player_win = False
        stones = 10
        while n >= stones:
            n -= stones
            stones -= 1
            player_win = not player_win
        return player_win