from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        idx1, idx2 = 0, 0
        ans = []
        while idx1 < len(firstList) and idx2 < len(secondList):
            interval1 = firstList[idx1]
            interval2 = secondList[idx2]

            if interval1[1] < interval2[0]:
                idx1 += 1
                if idx1 == len(firstList):
                    break
                continue
            if interval1[0] > interval2[1]:
                idx2 += 1
                if idx2 == len(secondList):
                    break
                continue

            if interval1[1] <= interval2[1]:
                ans.append([max(interval1[0], interval2[0]), min(interval1[1], interval2[1])])
                idx1 += 1
                if idx1 == len(firstList):
                    break
                continue

            if interval2[1] <= interval1[1]:
                ans.append([max(interval1[0], interval2[0]), min(interval1[1], interval2[1])])
                idx2 += 1
                if idx2 == len(secondList):
                    break
                continue
        return ans

data = [
    [[3, 5], [9, 20]]
    , [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
]
r = Solution().intervalIntersection(* data)
print(r)