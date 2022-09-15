from typing import List
from collections import Counter

class Solution:
    def get_gcd(self, narr: list[int]) -> int:
        gcd = min(narr)
        while gcd >= 1:
            found = True
            for n in narr:
               if n % gcd != 0:
                   found = False
                   break
            if found:
                return gcd
            gcd -= 1

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck_cnt = Counter(deck)
        gcd = self.get_gcd(list(deck_cnt.values()))
        return gcd >= 2

