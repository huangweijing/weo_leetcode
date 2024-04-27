from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for t in tickets:
            time += min(t, tickets[k] - 1)
        for i in range(k + 1):
            if tickets[i] >= tickets[k]:
                time += 1
        return time

