from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        if len(cnt1) == len(cnt2):
            if len(cnt1.keys() & cnt2.keys()) > 0:
                return True
            else:
                min1, max1 = min(cnt1.values()), max(cnt1.values())
                min2, max2 = min(cnt2.values()), max(cnt2.values())
                if max1 == 1 and min2 > 1:
                    return False
                elif min1 > 1 and max2 == 1:
                    return False
                else:
                    return True
        elif abs(len(cnt1) - len(cnt2)) >= 3:
            return False
        elif abs(len(cnt1) - len(cnt2)) in (1, 2):
            if len(cnt1) > len(cnt2):
                cnt1, cnt2 = cnt2, cnt1
            if abs(len(cnt1) - len(cnt2)) == 1:
                # add a type to cnt1
                for ch2, c2 in cnt2.items():
                    if ch2 not in cnt1 and c2 > 1:
                        for ch1, c1 in cnt1.items():
                            if c1 > 1 and ch1 in cnt2:
                                return True
                # remove a type from cnt2
                for ch2, c2 in cnt2.items():
                    if ch2 in cnt1 and c2 == 1:
                        for ch1, c1 in cnt1.items():
                            if ch1 in cnt2 and c1 > 1 and ch1 != ch2:
                                return True
                for ch2, c2 in cnt2.items():
                    if ch2 not in cnt1 and c2 == 1:
                        for ch1, c1 in cnt1.items():
                            if ch1 in cnt2 and c1 == 1 and ch1 != ch2:
                                return True
                return False
            elif abs(len(cnt1) - len(cnt2)) == 2:
                for ch2, c2 in cnt2.items():
                    if ch2 not in cnt1 and c2 == 1:
                        for ch1, c1 in cnt1.items():
                            if ch1 in cnt2 and c1 > 1:
                                return True
                return False
            

        
