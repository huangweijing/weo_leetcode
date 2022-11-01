class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        acnt, bcnt = 0, 0
        for i, ch in enumerate(colors):
            if 0 < i < len(colors) - 1  and \
                colors[i] == colors[i - 1] == colors[i + 1]:
                if colors[i] == "A":
                    acnt += 1
                else:
                    bcnt += 1
        return acnt > bcnt
