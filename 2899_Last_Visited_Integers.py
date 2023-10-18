from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ans, arr = [], []
        prev_cnt = 0
        for word in words:
            if word == "prev":
                prev_cnt += 1
                if prev_cnt > len(arr):
                    ans.append(-1)
                else:
                    ans.append(arr[-prev_cnt])
            else:
                arr.append(int(word))
                prev_cnt = 0
        return ans
