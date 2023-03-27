from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        chg = [0] * 3
        for bill in bills:
            print(chg)
            if bill == 5:
                chg[0] += 1
            elif bill == 10:
                if chg[0] == 0:
                    return False
                chg[0] -= 1
                chg[1] += 1
            elif bill == 20:
                if chg[1] == 0:
                    if chg[0] < 3:
                        return False
                    else:
                        chg[0] -= 3
                        chg[2] += 1
                else:
                    if chg[0] == 0:
                        return False
                    else:
                        chg[0] -= 1
                        chg[1] -= 1
                        chg[2] += 1

        return True


bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
r = Solution().lemonadeChange(bills)
print(r)