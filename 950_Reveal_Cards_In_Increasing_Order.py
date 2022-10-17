from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [0] * len(deck)
        q = deque(range(len(ans)))
        for num in deck:
            idx = q.popleft()
            ans[idx] = num
            if len(q) > 0:
                q.append(q.popleft())
        return ans

data_deck = [17,13,11,2,3,5,7]
r = Solution().deckRevealedIncreasing(data_deck)
print(r)
