from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        alice_score, bob_score = 0, 0
        for i, v in enumerate(reversed(sorted(zip(aliceValues, bobValues), key=lambda x: sum(x)))):
            if i & 1 == 0:
                alice_score += v[0]
            else:
                bob_score += v[1]
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        return 0