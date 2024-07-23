from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        bob_score = sum(-1 if p == 0 else 1 for p in possible)
        alice_score = 0
        level = 0
        for p in possible[: -1]:
            level += 1
            alice_score += -1 if p == 0 else 1
            bob_score -= -1 if p == 0 else 1
            if alice_score > bob_score:
                return level
        return -1