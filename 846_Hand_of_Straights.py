from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        cnt = Counter(hand)
        key_list = list(sorted(hand, reverse=True))
        while len(cnt) > 0:
            key = key_list.pop()
            while key not in cnt:
                key = key_list.pop()
            for i in range(key, key + groupSize):
                if i not in cnt:
                    return False
                cnt[i] -= 1
                if cnt[i] == 0:
                    del cnt[i]
        return True



data = [
    [1,2,3,6,2,3,4,7,8]
    , 3
]
r = Solution().isNStraightHand(* data)
print(r)
