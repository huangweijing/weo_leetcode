from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = score.copy()
        rank.sort(reverse=True)
        score_dic = dict[int, int]()
        for r, s in enumerate(rank):
            score_dic[s] = r + 1
        result = list[str]()
        for s in score:
            r = score_dic[s]
            if r == 1:
                result.append("Gold Medal")
            elif r == 2:
                result.append("Silver Medal")
            elif r == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(r))
        return result


