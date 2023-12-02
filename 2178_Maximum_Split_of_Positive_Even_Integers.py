from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1 == 1:
            return []
        num, ans = 2, []
        while True:
            if finalSum >= num * 2 + 2:
                ans.append(num)
                finalSum -= num
            else:
                ans.append(finalSum)
                return ans
            num += 2
